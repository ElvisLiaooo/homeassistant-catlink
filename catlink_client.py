import base64
import datetime
import hashlib
import logging
import time

from aiohttp import ClientSession, ClientConnectorError
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from homeassistant.const import CONF_TOKEN, CONF_DEVICES
from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store
from tzlocal import get_localzone_name

from .const import *
from .data_model import CatlinkData, Feeder, WaterFountain, LitterBox
from .exceptions import AuthError, NoDevicesError

_LOGGER = logging.getLogger(__name__)

TIMEOUT = 5 * 60


class CatlinkClient:
    def __init__(self, phone: str, password: str,
                 session: ClientSession | None = None, timeout: int = TIMEOUT) -> None:
        self.phone: str = phone
        self.pwd: str = password
        self.base_url: str = ''
        self._session: ClientSession = session if session else ClientSession()
        self.tz: str = get_localzone_name()
        self.timeout: int = timeout
        self.token: str | None = None

    @property
    def password(self):
        password = self.pwd
        if len(password) <= 16:
            password = self.encrypt_password(password)
        return password

    async def request(self, api, pms=None, method='GET', **kwargs):
        method = method.upper()
        pms_cloned = pms.copy()
        url = self.api_url(api)
        kws = {
            'timeout': 60,
            'headers': {
                'language': 'zh_CN',
                'User-Agent': 'okhttp/3.10.0',
            },
        }
        kws.update(kwargs)
        if pms_cloned is None:
            pms_cloned = {}
        pms_cloned['noncestr'] = int(time.time() * 1000)
        if self.token:
            pms_cloned[CONF_TOKEN] = self.token
        pms_cloned['sign'] = self.params_sign(pms_cloned)
        if method in ['GET']:
            kws['params'] = pms_cloned
        elif method in ['POST_GET']:
            method = 'POST'
            kws['params'] = pms_cloned
        else:
            kws['data'] = pms_cloned
        try:
            # _LOGGER.warning('Req %s, %s, %s', method, url, kws)
            req = await self._session.request(method, url, **kws)
            resp = await req.json() or {}
            # _LOGGER.warning('Resp %s', resp)
            return resp
        except (ClientConnectorError, TimeoutError) as exc:
            _LOGGER.error('Request api failed: %s', [method, url, pms_cloned, exc])
        return {}

    def api_url(self, api=''):
        if api[:6] == 'https:' or api[:5] == 'http:':
            return api
        bas = DEFAULT_API_BASE
        return f"{bas.rstrip('/')}/{api.lstrip('/')}"

    async def async_login(self, hass: HomeAssistant):
        pms = {
            'platform': 'ANDROID',
            'internationalCode': '86',
            'mobile': self.phone,
            'password': self.password,
        }
        self.token = None

        response = await self.request('login/password', pms, 'POST')
        if response['returnCode'] == 2002:
            raise AuthError('username or password is incorrect! login failed! msg:%s', response['msg'])
        token = response.get('data', {}).get('token')
        if not token:
            _LOGGER.error('Login %s failed: %s', self.phone, [response, pms])
            return False
        self.token = token
        await self.async_check_auth(hass, True)
        return True

    async def async_check_auth(self, hass: HomeAssistant, save=False):
        fileName = f'{DOMAIN}/auth-{self.phone}.json'
        store = Store(hass, 1, fileName)
        old = await store.async_load() or {}
        if save:
            cfg = {
                CONF_PHONE: self.phone,
                CONF_TOKEN: self.token,
            }
            if cfg.get(CONF_TOKEN) == old.get(CONF_TOKEN):
                cfg['update_at'] = old.get('update_at')
            else:
                cfg['update_at'] = f'{datetime.datetime.today()}'
            await store.async_save(cfg)
            return cfg
        if old.get(CONF_TOKEN):
            self.token = old.get(CONF_TOKEN)
        else:
            await self.async_login(hass)
        return old

    async def get_devices(self, hass: HomeAssistant):
        await self.async_check_auth(hass)
        own_list = await self.get_devices_0('token/device/union/ownList', hass)
        shared_list = await self.get_devices_0('token/device/union/sharedList', hass)

        device_dict = dict()
        for device in own_list:
            if device['id'] not in device_dict:
                device_dict[device['id']] = device
        for device in shared_list:
            if device['id'] not in device_dict:
                device_dict[device['id']] = device

        device_list = device_dict.values()
        if not device_list:
            _LOGGER.warning(
                'Got devices for %s failed, \nowned:%s \nshared:%s', self.phone, own_list, shared_list)
        return device_list

    async def get_devices_0(self, api: str, hass: HomeAssistant):
        rsp = await self.request(api, {'type': 'NONE'})
        eno = rsp.get('returnCode', 0)
        if eno == 1002:  # Illegal token
            if await self.async_login(hass):
                rsp = await self.request(api)
        device_list = rsp.get('data', {}).get(CONF_DEVICES) or []
        return device_list

    @staticmethod
    def params_sign(pms: dict):
        lst = list(pms.items())
        lst.sort()
        pms = [
            f'{k}={v}'
            for k, v in lst
        ]
        pms.append(f'key={SIGN_KEY}')
        pms = '&'.join(pms)
        return hashlib.md5(pms.encode()).hexdigest().upper()

    @staticmethod
    def encrypt_password(pwd):
        pwd = f'{pwd}'
        md5 = hashlib.md5(pwd.encode()).hexdigest().lower()
        sha = hashlib.sha1(md5.encode()).hexdigest().upper()
        pub = serialization.load_der_public_key(base64.b64decode(RSA_PUBLIC_KEY), default_backend())
        pad = padding.PKCS1v15()
        return base64.b64encode(pub.encrypt(sha.encode(), pad)).decode()

    async def get_catlink_data(self, hass: HomeAssistant) -> CatlinkData:
        """Fetch data for all Catlink devices."""

        device_list = await self.get_devices(hass)


        fountains_data: dict[int, WaterFountain] = {}
        feeders_data: dict[int, Feeder] = {}
        litter_boxes_data: dict[int, LitterBox] = {}

        if device_list:
            for device in device_list:
                if device['deviceType'] in DETAIL_URL_MAPPING:
                    device_type = device['deviceType']
                    device_id = device['id']

                    params = {'deviceId': device_id}
                    detail_url = DETAIL_URL_MAPPING[device_type]
                    try:
                        device_detail_response = await self.request(detail_url, params)
                        detail_data = device_detail_response.get('data', {}).get('deviceInfo') or {}
                    except (TypeError, ValueError) as exc:
                        detail_data = []
                        _LOGGER.error('Got device logs for %s failed: %s', device_type, device_detail_response)

                    event_url = LOG_URL_MAPPING[device_type]
                    try:
                        event_response = await self.request(event_url, params)
                        event_data = event_response.get('data', {}).get(LOG_DATA_NODE_MAPPING[device_type]) or []
                    except (TypeError, ValueError) as exc:
                        event_data = []
                        _LOGGER.error('Got device logs for %s failed: %s', device_type, event_response)

                    if device_type == 'PURE3':
                        fountains_data[device_id] = await self.get_water_fountain(device, detail_data, event_data)
                    elif device_type == 'FEEDER':
                        feeders_data[device_id] = Feeder(id=device_id,
                                                         device_attrs=device,
                                                         device_detail=detail_data,
                                                         event_record=event_data,
                                                         type=device_type)
                    elif device_type == 'SCOOPER':
                        litter_boxes_data[device_id] = LitterBox(id=device_id,
                                                                 device_attrs=device,
                                                                 device_detail=detail_data,
                                                                 event_record=event_data,
                                                                 type=device_type)
        return CatlinkData(uid=self.phone,
                           water_fountains=fountains_data, feeders=feeders_data, litter_boxes=litter_boxes_data)

    async def get_water_fountain(self, device_attr, detail_data, event_data) -> WaterFountain:
        device_type = device_attr['deviceType']
        device_id = device_attr['id']

        fountain_cat_data_url = CAT_STATISTIC_MAPPING[device_type]
        cat_data_param = {
            'deviceId': device_id,
            'pageNumber': 1,
            'pageSize': 3
        }
        try:
            fountain_cat_data_response = await self.request(fountain_cat_data_url, cat_data_param)
            fountain_cat_data = fountain_cat_data_response.get('data', {}).get('catInfo', {}).get('singleData') or []
        except (TypeError, ValueError) as exc:
            fountain_cat_data = []
            _LOGGER.error('Got cat statistic for %s failed: %s', device_type, fountain_cat_data_response)

        return WaterFountain(id=device_id,
                             device_attrs=device_attr,
                             device_detail=detail_data,
                             event_record=event_data,
                             cat_data=fountain_cat_data,
                             device_type=device_type)
