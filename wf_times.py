import asyncio
import logging
from datetime import time, datetime
from typing import Any

from homeassistant.components.time import TimeEntity
from homeassistant.const import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .data_model import WaterFountain
from .coordinator import CatlinkDevicesCoordinator
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class WaterFountainNightModeStartTime(CoordinatorEntity, TimeEntity):

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
                + '_' + str(self.fountain_data.id) + '_night_mode_start_time')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "water_fountain_night_mode_start_time"

    @property
    def icon(self) -> str | None:
        return 'mdi:bed-clock'

    @property
    def entity_category(self) -> EntityCategory | None:
        return EntityCategory.CONFIG

    @property
    def native_value(self) -> time | None:
        time_str = self.fountain_data.device_detail['nightModeStartTime']
        if time_str:
            return datetime.strptime(time_str, '%H:%M').time()
        else:
            return None

    async def async_set_value(self, value: time) -> None:
        if not self.fountain_data.device_detail['nightModeFlag']:
            return
        api = 'token/device/purepro/nightmode'
        time_str = value.strftime('%H:%M')
        params = {
            'deviceId': self.fountain_data.id,
            'switchFlag': 1,
            'startTime': time_str,
            'endTime': self.fountain_data.device_detail['nightModeEndTime']
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['nightModeStartTime'] = time_str
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class WaterFountainNightModeEndTime(CoordinatorEntity, TimeEntity):

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
                + '_' + str(self.fountain_data.id) + '_night_mode_end_time')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "water_fountain_night_mode_end_time"

    @property
    def icon(self) -> str | None:
        return 'mdi:bed-clock'

    @property
    def entity_category(self) -> EntityCategory | None:
        return EntityCategory.CONFIG

    @property
    def native_value(self) -> time | None:
        time_str = self.fountain_data.device_detail['nightModeEndTime']
        if time_str:
            return datetime.strptime(time_str, '%H:%M').time()
        else:
            return None

    async def async_set_value(self, value: time) -> None:
        if not self.fountain_data.device_detail['nightModeFlag']:
            return
        api = 'token/device/purepro/nightmode'
        time_str = value.strftime('%H:%M')
        params = {
            'deviceId': self.fountain_data.id,
            'switchFlag': 1,
            'startTime': self.fountain_data.device_detail['nightModeStartTime'],
            'endTime': time_str
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['nightModeEndTime'] = time_str
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)
