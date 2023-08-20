from homeassistant.const import Platform

DOMAIN = 'elvis-catlink'
CONF_ACCOUNTS = 'accounts'
CONF_API_BASE = 'api_base'
CONF_USER_ID = 'uid'
CONF_PHONE = 'phone'
CONF_PHONE_IAC = 'phone_iac'
CONF_LANGUAGE = 'language'
POLLING_INTERVAL = "polling_interval"
CATLINK_COORDINATOR = "catlink_coordinator"
UPDATE_LISTENER = "update_listener"

PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    # Platform.FAN,
    # Platform.NUMBER,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.SWITCH,
    Platform.TIME
    # Platform.TEXT
]


TIMEOUT = 5 * 60
SIGN_KEY = '00109190907746a7ad0e2139b6d09ce47551770157fe4ac5922f3a5454c82712'
RSA_PUBLIC_KEY = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCCA9I+iEl2AI8dnhdwwxPxHVK8iNAt6aTq6UhNsLsguWS5qtbLnuGz2RQdfNS' \
                 'aKSU2B6D/vE2gb1fM6f1A5cKndqF/riWGWn1EfL3FFQZduOTxoA0RTQzhrTa5LHcJ/an/NuHUwShwIOij0Mf4g8faTe4FT7/HdA' \
                 'oK7uW0cG9mZwIDAQAB'
RSA_PRIVATE_KEY = 'MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAIID0j6ISXYAjx2eF3DDE/EdUryI0C3ppOrpSE2wuyC5ZLmq1s' \
                  'ue4bPZFB181JopJTYHoP+8TaBvV8zp/UDlwqd2oX+uJYZafUR8vcUVBl245PGgDRFNDOGtNrksdwn9qf824dTBKHAg6KPQx/iD' \
                  'x9pN7gVPv8d0Cgru5bRwb2ZnAgMBAAECgYAccTuQRH5Vmz+zyf70wyhcqf6Mkh2Avck/PrN7k3sMaKJZX79HokVb89RLsyBLbU' \
                  '7fqAGXkJkmzNTXViT6Colvi1T7QQWhkvPsPEsu/89s5yo0ME2+rtvBA/niy1iQs6UYTzZivSKosLVgCTmcOYbp5eUCP8IPtKy/' \
                  '3vzkIBMZqQJBALn0bAgCeXwctYqznCboNHAX7kGk9HjX8VCOfaBh1WcAYWk7yKzYZemMKXMw5ifeopT0uUpLEk5mlN4nxwBsTp' \
                  'sCQQCy/SHTlQyt/yauVyrJipZflUK/hq6hIZFIu1Mc40L6BDNAboi42P9suznXbV7DD+LNpxFnkYlee8sitY0R474lAkEAsjBV' \
                  'lRdJ8nRQQij6aQ35sbA8zwqSeXnz842XNCiLpbfnoD95fKeggLuevJMO+QWOJc6b/2UQlbAW1wqm1vDyIQJAUhYVNVvd/M5Phx' \
                  'Ui4ltUq3Fgs0WpQOyMHLcMXus7BD544svOmDesrMkQtePK2dqnQXmlWcI9Jb/QYZKxp8qyoQJAP2kK4dc3AA4BDVQUMHYiSnGp' \
                  'I0eGQrD/W4rBeoCX8sJDCH49lMsec52TFI2Gn8tTKOCqqgGvRSKDJ005HlnmKw=='
DEFAULT_API_BASE = 'https://app.catlinks.cn/api/'

DETAIL_URL_MAPPING = {
    'PURE3': 'token/device/purepro/pure3/detail',
    'FEEDER': 'token/device/feeder/detail',
    'SCOOPER': 'token/device/info'
}

LOG_URL_MAPPING = {
    'PURE3': 'token/device/purepro/stats/log/top5',
    'FEEDER': 'token/device/feeder/stats/log/top5',
    'SCOOPER': 'token/device/scooper/stats/log/top5'
}

CAT_STATISTIC_MAPPING = {
    'PURE3': 'token/device/purepro/stats/catDataList'
}

WATER_FOUNTAIN_RUN_MODE = {
    'CONTINUOUS_SPRING': '持续涌泉',
    'INDUCTION_SPRING': '感应涌泉',
    'INTERMITTENT_SPRING': '间歇涌泉',
}