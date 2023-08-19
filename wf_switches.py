import asyncio
import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.const import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .data_model import WaterFountain
from .coordinator import CatlinkDevicesCoordinator
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class WaterFountainChildLock(CoordinatorEntity, SwitchEntity):

    def __init__(self, coordinator: CatlinkDevicesCoordinator, fountain_id):
        super().__init__(coordinator)
        self.fountain_id = fountain_id

    @property
    def fountain_data(self) -> WaterFountain:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.water_fountains[self.fountain_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.fountain_data.id)},
            "name": self.fountain_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.fountain_data.device_attrs['deviceType'],
            "sw_version": f'{self.fountain_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_child_lock')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "water_fountain_child_lock"

    @property
    def is_on(self) -> bool:
        return self.fountain_data.device_detail['childLock'] == 0

    @property
    def available(self) -> bool:
        return self.fountain_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        if self.is_on:
            return 'mdi:lock-check-outline'
        else:
            return 'mdi:lock-open-outline'

    async def async_turn_on(self, **kwargs) -> None:
        api = 'token/device/purepro/keyLock/setting'
        params = {
            'deviceId': self.fountain_data.id,
            'lockStatus': 1
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['childLock'] = 0
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

    async def async_turn_off(self, **kwargs) -> None:
        api = 'token/device/purepro/keyLock/setting'
        params = {
            'deviceId': self.fountain_data.id,
            'lockStatus': 0
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['childLock'] = 1
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class WaterFountainIndicatorLight(CoordinatorEntity, SwitchEntity):

    def __init__(self, coordinator: CatlinkDevicesCoordinator, fountain_id):
        super().__init__(coordinator)
        self.fountain_id = fountain_id

    @property
    def fountain_data(self) -> WaterFountain:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.water_fountains[self.fountain_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.fountain_data.id)},
            "name": self.fountain_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.fountain_data.device_attrs['deviceType'],
            "sw_version": f'{self.fountain_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_indicator_light')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "water_fountain_indicator_light"

    @property
    def is_on(self) -> bool:
        return self.fountain_data.device_detail['pureLightStatus'] == 'OPEN'

    @property
    def available(self) -> bool:
        return self.fountain_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        if self.is_on:
            return 'mdi:lightbulb'
        else:
            return 'mdi:lightbulb-off'

    async def async_turn_on(self, **kwargs) -> None:
        api = 'token/device/purepro/light/setting'
        params = {
            'deviceId': self.fountain_data.id,
            'status': 'OPEN'
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['pureLightStatus'] = 'OPEN'
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

    async def async_turn_off(self, **kwargs) -> None:
        api = 'token/device/purepro/light/setting'
        params = {
            'deviceId': self.fountain_data.id,
            'status': 'CLOSE'
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['pureLightStatus'] = 'CLOSE'
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class WaterFountainIndicatorSound(CoordinatorEntity, SwitchEntity):

    def __init__(self, coordinator: CatlinkDevicesCoordinator, fountain_id):
        super().__init__(coordinator)
        self.fountain_id = fountain_id

    @property
    def fountain_data(self) -> WaterFountain:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.water_fountains[self.fountain_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.fountain_data.id)},
            "name": self.fountain_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.fountain_data.device_attrs['deviceType'],
            "sw_version": f'{self.fountain_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_indicator_sound')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "water_fountain_indicator_sound"

    @property
    def is_on(self) -> bool:
        return self.fountain_data.device_detail['keyTone'] == 0

    @property
    def available(self) -> bool:
        return self.fountain_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        if self.is_on:
            return 'mdi:volume-medium'
        else:
            return 'mdi:volume-off'

    async def async_turn_on(self, **kwargs) -> None:
        api = 'token/device/purepro/keyTone/setting'
        params = {
            'deviceId': self.fountain_data.id,
            'lockStatus': 1
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['keyTone'] = 1
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

    async def async_turn_off(self, **kwargs) -> None:
        api = 'token/device/purepro/keyTone/setting'
        params = {
            'deviceId': self.fountain_data.id,
            'lockStatus': 0
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['keyTone'] = 0
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class WaterFountainNightModeSwitch(CoordinatorEntity, SwitchEntity):

    def __init__(self, coordinator: CatlinkDevicesCoordinator, fountain_id):
        super().__init__(coordinator)
        self.fountain_id = fountain_id

    @property
    def fountain_data(self) -> WaterFountain:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.water_fountains[self.fountain_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.fountain_data.id)},
            "name": self.fountain_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.fountain_data.device_attrs['deviceType'],
            "sw_version": f'{self.fountain_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_night_mode_switch')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "water_fountain_night_mode_switch"

    @property
    def is_on(self) -> bool:
        return self.fountain_data.device_detail['nightModeFlag']

    @property
    def available(self) -> bool:
        return self.fountain_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        return 'mdi:lightbulb-night-outline'

    @property
    def entity_category(self) -> EntityCategory | None:
        return EntityCategory.CONFIG

    async def async_turn_on(self, **kwargs) -> None:
        api = 'token/device/purepro/nightmode'
        params = {
            'deviceId': self.fountain_data.id,
            'switchFlag': 1,
            'startTime': self.fountain_data.device_detail['nightModeStartTime'],
            'endTime': self.fountain_data.device_detail['nightModeEndTime']
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['nightModeFlag'] = True
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

    async def async_turn_off(self, **kwargs) -> None:
        api = 'token/device/purepro/nightmode'
        params = {
            'deviceId': self.fountain_data.id,
            'switchFlag': 0,
            'startTime': '',
            'endTime': ''
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['nightModeFlag'] = False
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)