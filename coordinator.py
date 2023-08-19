import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PASSWORD, CONF_DEVICES
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .catlink_client import CatlinkClient
from .const import CONF_PHONE, TIMEOUT, DOMAIN, POLLING_INTERVAL
from .data_model import CatlinkData
from .exceptions import AuthError

_LOGGER = logging.getLogger(__name__)


class CatlinkDevicesCoordinator(DataUpdateCoordinator):

    data: CatlinkData

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self.client = CatlinkClient(
            entry.data[CONF_PHONE],
            entry.data[CONF_PASSWORD],
            session=async_get_clientsession(hass),
            timeout=TIMEOUT,
        )
        super().__init__(
            hass,
            _LOGGER,
            name=f'{DOMAIN}-{entry.data[CONF_PHONE]}-{CONF_DEVICES}',
            update_interval=timedelta(seconds=entry.options[POLLING_INTERVAL]),
        )
        self._subs = {}

    async def _async_update_data(self) -> CatlinkData:
        """Fetch data from Catlink."""

        try:
            data = await self.client.get_catlink_data(self.hass)
            _LOGGER.debug(f'Found the following Catlink devices/pets: {data}')
        except AuthError as error:
            raise ConfigEntryAuthFailed(error) from error
        else:
            return data
