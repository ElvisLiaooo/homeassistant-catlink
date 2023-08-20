import asyncio
import logging
from typing import Any
from datetime import time, datetime

from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass
from homeassistant.components.button import ButtonEntity
from homeassistant.components.select import SelectEntity
from homeassistant.components.sensor import (
    SensorEntity, SensorStateClass, SensorDeviceClass,
)
from homeassistant.components.switch import SwitchEntity
from homeassistant.components.time import TimeEntity
from homeassistant.const import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .data_model import WaterFountain
from .const import DOMAIN, WATER_FOUNTAIN_RUN_MODE
from .coordinator import CatlinkDevicesCoordinator

_LOGGER = logging.getLogger(__name__)
WATER_FOUNTAIN_RUN_MODE_OPTION_MAPPING = {v: k for k, v in WATER_FOUNTAIN_RUN_MODE.items()}


class WaterFountainStatus(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_status')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_main_status"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.fountain_data.device_detail['subDesc'] or 'Unknown'

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:information'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class WaterFountainWaterLevel(CoordinatorEntity, SensorEntity):
    """Representation of water fountain status."""

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_water_level')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_water_level_num"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.fountain_data.device_detail['waterLevelNum'] or 'Unknown'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC

    @property
    def state_class(self) -> SensorStateClass:
        """Return the type of state class."""
        return SensorStateClass.MEASUREMENT

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:water-pump'

    @property
    def native_unit_of_measurement(self) -> str | None:
        return '%'


class WaterFountainWaterLevelDesc(CoordinatorEntity, SensorEntity):

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_water_level_desc')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_water_level_desc"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.fountain_data.device_detail['waterLevelStrDescription'] or 'Unknown'

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:water-pump'


class FilterRemainDays(CoordinatorEntity, SensorEntity):
    """Representation of water fountain status."""

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_filter_remain_days')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_filter_remain_days"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.fountain_data.device_detail['filterElementTimeCountdown']

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC

    @property
    def state_class(self) -> SensorStateClass:
        """Return the type of state class."""
        return SensorStateClass.MEASUREMENT

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:counter'

    @property
    def native_unit_of_measurement(self) -> str | None:
        return 'Days'


class WaterFountainRunMode(CoordinatorEntity, SensorEntity):
    """Representation of water fountain status."""

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_run_mode')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_run_mode"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return WATER_FOUNTAIN_RUN_MODE[self.fountain_data.device_detail['runMode']] or "Unknown"

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:water-outline'


class LastDrinkEvent(CoordinatorEntity, SensorEntity):
    """Representation of water fountain status."""

    last_data: str = "Unknown"

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_last_drink_event')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_last_drink_event"

    @property
    def native_value(self) -> str | None:
        logs = self.fountain_data.event_record
        if not logs:
            return self.last_data
        filtered = list(filter(lambda x: x['type'] == 'DRINK', logs))
        if not filtered:
            return self.last_data
        filtered.sort(key=lambda x: int(x['id']), reverse=True)

        result = filtered[0]
        return result['time'] + '  ' + result['event']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:cup-water'


class LastFountainEvent(CoordinatorEntity, SensorEntity):
    """Representation of water fountain status."""

    last_data: str

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_last_fountain_event')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_last_fountain_event"

    @property
    def native_value(self) -> str | None:
        logs = self.fountain_data.event_record
        if not logs:
            return self.last_data
        filtered = list(filter(lambda x: x['type'] != 'DRINK', logs))
        if not filtered:
            return self.last_data
        filtered.sort(key=lambda x: int(x['id']), reverse=True)

        result = filtered[0]
        return result['time'] + '  ' + result['event']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:information-box-outline'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class CatDrinkTotalTimeToday(CoordinatorEntity, SensorEntity):

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_drink_total_time')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_drink_total_time"

    @property
    def native_value(self) -> str | None:
        return self.fountain_data.cat_data['duration']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:cat'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class CatDrinkCountToday(CoordinatorEntity, SensorEntity):

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_drink_count_today')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_drink_count_today"

    @property
    def native_value(self) -> str | None:
        return self.fountain_data.cat_data['intakesOrTimes']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:cat'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


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


class WaterFountainFluffyHair(CoordinatorEntity, ButtonEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_fluffy_hair')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_fluffy_hair"

    @property
    def available(self) -> bool:
        return self.fountain_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:hair-dryer-outline'

    async def async_press(self) -> None:
        api = 'token/device/purepro/fluffyHair'
        params = {
            'deviceId': self.fountain_data.id,
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class WaterFountainRunModeSelect(CoordinatorEntity, SelectEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, fountain_id):
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
        """Sets unique ID for this entity."""
        return (self.fountain_data.device_detail['deviceName']
                + '_' + str(self.fountain_data.id) + '_run_mode_select')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "water_fountain_run_mode_select"

    @property
    def available(self) -> bool:
        return self.fountain_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:water-outline'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.CONFIG

    @property
    def current_option(self) -> str:
        current_mode = self.fountain_data.device_detail['runMode']
        return WATER_FOUNTAIN_RUN_MODE[current_mode]

    @property
    def options(self) -> list[str]:
        return list(WATER_FOUNTAIN_RUN_MODE.values())

    async def async_select_option(self, option: str) -> None:
        api = 'token/device/purepro/runMode'
        selected_mode = WATER_FOUNTAIN_RUN_MODE_OPTION_MAPPING[option]
        params = {
            'deviceId': self.fountain_data.id,
            'runMode': selected_mode,
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.fountain_data.device_detail['runMode'] = selected_mode
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class WaterFountainNightMode(CoordinatorEntity, BinarySensorEntity):

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
                + '_' + str(self.fountain_data.id) + '_on_night_mode')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "water_fountain_on_night_mode"

    @property
    def device_class(self) -> BinarySensorDeviceClass:
        """Return entity device class."""

        return BinarySensorDeviceClass.RUNNING

    @property
    def is_on(self) -> bool:
        return self.fountain_data.device_detail['onNightMode']

    @property
    def available(self) -> bool:
        return self.fountain_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        if self.is_on:
            return 'mdi:weather-night'
        else:
            return 'mdi:sun-clock-outline'


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
