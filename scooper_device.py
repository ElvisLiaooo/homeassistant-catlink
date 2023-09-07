import asyncio
import logging
from typing import Any
from datetime import time, datetime

from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass
from homeassistant.components.button import ButtonEntity
from homeassistant.components.select import SelectEntity
from homeassistant.components.sensor import (
    SensorEntity, SensorStateClass,
)
from homeassistant.components.switch import SwitchEntity
from homeassistant.components.time import TimeEntity
from homeassistant.const import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .data_model import LitterBox
from .const import DOMAIN, WATER_FOUNTAIN_RUN_MODE, SCOOPER_WORK_STATUS_DESC, SCOOPER_WORK_MODES_NAME, \
    SCOOPER_WORK_MODES_NAME_MAPPING, SCOOPER_INDICATOR_LIGHT_NAME, SCOOPER_INDICATOR_LIGHT_NAME_MAPPING
from .coordinator import CatlinkDevicesCoordinator

_LOGGER = logging.getLogger(__name__)


class LitterWeightStatus(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + 'litter_weight_status')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_litter_weight_status"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.scooper_data.device_detail['weight']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:weight'


class LitterWorkStatus(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_litter_work_status')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_litter_work_status"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return SCOOPER_WORK_STATUS_DESC[self.scooper_data.device_detail['workStatus']]

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:information-slab-box-outline'


class LitterCurrentMessage(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_litter_current_message')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_litter_current_message"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.scooper_data.device_detail['currentMessage']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:information-slab-box-outline'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class LitterInductionCleanTimes(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_litter_induction_clean_times')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_litter_induction_clean_times"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.scooper_data.device_detail['inductionTimes']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:induction'


class LitterManualCleanTimes(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_litter_manual_clean_times')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_litter_manual_clean_times"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.scooper_data.device_detail['manualTimes']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:hand-back-left-outline'


class LitterAllClearTimes(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_litter_all_clear_times')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_litter_all_clear_times"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.scooper_data.device_detail['clearTimes']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:delete-empty-outline'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class LitterTimingCleanTimes(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_litter_timing_clean_times')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_litter_timing_clean_times"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.scooper_data.device_detail['timerTimes']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:calendar-clock'


class LastWCEvent(CoordinatorEntity, SensorEntity):
    """Representation of water fountain status."""

    last_data: str = "Unknown"

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + 'scooper_wc_event')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_last_wc_event"

    @property
    def native_value(self) -> str | None:
        logs = self.scooper_data.event_record
        if not logs:
            return self.last_data
        filtered = list(filter(lambda x: x['type'] == 'WC', logs))
        if not filtered:
            return self.last_data
        filtered.sort(key=lambda x: int(x['id']), reverse=True)

        result = filtered[0]
        self.last_data = result['time'] + ', ' + result['event'] + ', ' + result['firstSection'] + ', ' + result['secondSection']
        return self.last_data

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:toilet'


class LastCleanEvent(CoordinatorEntity, SensorEntity):
    """Representation of water fountain status."""

    last_data: str = "Unknown"

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + 'scooper_clean_event')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_last_clean_event"

    @property
    def native_value(self) -> str | None:
        logs = self.scooper_data.event_record
        if not logs:
            return self.last_data
        filtered = list(filter(lambda x: x['type'] != 'WC', logs))
        if not filtered:
            return self.last_data
        filtered.sort(key=lambda x: int(x['id']), reverse=True)

        result = filtered[0]
        self.last_data = ', '.join((result['time'], result['event'], result['firstSection']))
        return self.last_data

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:information-box-outline'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class ScooperWifiStatus(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_wifi_status')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_wifi_status"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.scooper_data.wifi_info['wifiStatus']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:wifi'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class ScooperWifiStrength(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_wifi_strength')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_wifi_strength"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.scooper_data.wifi_info['wifiSignalPercent']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:wifi'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class ScooperWifiRssi(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_wifi_rssi')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_wifi_rssi"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.scooper_data.wifi_info['rssi']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:wifi'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class ScooperRunModeSelect(CoordinatorEntity, SelectEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_run_mode_select')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_run_mode_select"

    @property
    def available(self) -> bool:
        return self.scooper_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:vacuum-outline'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.CONFIG

    @property
    def current_option(self) -> str:
        current_mode = self.scooper_data.device_detail['workModel']
        return SCOOPER_WORK_MODES_NAME[current_mode]

    @property
    def options(self) -> list[str]:
        return list(SCOOPER_WORK_MODES_NAME.values())

    async def async_select_option(self, option: str) -> None:
        api = 'token/device/changeMode'
        selected_mode = SCOOPER_WORK_MODES_NAME_MAPPING[option]
        params = {
            'deviceId': self.scooper_data.id,
            'workModel': selected_mode,
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['workModel'] = selected_mode
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class ScooperSafeDelayCleanTimeSelect(CoordinatorEntity, SelectEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_safe_clean_delay_time_select')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_safe_clean_delay_time_select"

    @property
    def available(self) -> bool:
        return self.scooper_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:timer-cog-outline'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.CONFIG

    @property
    def current_option(self) -> str:
        return self.scooper_data.device_detail['safeTime']

    @property
    def options(self) -> list[str]:
        return ['1', '3', '5', '7', '10', '15', '30']

    async def async_select_option(self, option: str) -> None:
        api = 'token/device/safeTimeSetting'
        params = {
            'deviceId': self.scooper_data.id,
            'safeTime': option,
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['safeTime'] = option
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class ScooperIndicatorLightMode(CoordinatorEntity, SelectEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_indicator_light_mode')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_indicator_light_mode"

    @property
    def available(self) -> bool:
        return self.scooper_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:car-light-dimmed'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.CONFIG

    @property
    def current_option(self) -> str:
        return SCOOPER_INDICATOR_LIGHT_NAME[self.scooper_data.device_detail['indicatorLight']]

    @property
    def options(self) -> list[str]:
        return list(SCOOPER_INDICATOR_LIGHT_NAME.values())

    async def async_select_option(self, option: str) -> None:
        api = 'token/device/indicatorLightSetting'
        selected_mode = SCOOPER_INDICATOR_LIGHT_NAME_MAPPING[option]
        params = {
            'deviceId': self.scooper_data.id,
            'status': selected_mode,
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['indicatorLight'] = selected_mode
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class ScooperActionStart(CoordinatorEntity, ButtonEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_manual_clean_start')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_manual_clean_start"

    @property
    def available(self) -> bool:
        return self.scooper_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:play-outline'

    async def async_press(self) -> None:
        api = 'token/device/actionCmd'
        params = {
            'deviceId': self.scooper_data.id,
            'cmd': '01'
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['workStatus'] = '01'
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class ScooperActionPause(CoordinatorEntity, ButtonEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_manual_clean_pause')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "scooper_manual_clean_pause"

    @property
    def available(self) -> bool:
        return self.scooper_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:pause-circle-outline'

    async def async_press(self) -> None:
        api = 'token/device/actionCmd'
        params = {
            'deviceId': self.scooper_data.id,
            'cmd': '00'
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['workStatus'] = '00'
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class ScooperNightModeStartTime(CoordinatorEntity, TimeEntity):

    start_time: str = '00:00'

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_night_mode_start_time')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "scooper_night_mode_start_time"

    @property
    def icon(self) -> str | None:
        return 'mdi:bed-clock'

    @property
    def entity_category(self) -> EntityCategory | None:
        return EntityCategory.CONFIG

    @property
    def native_value(self) -> time | None:
        return datetime.strptime(self.start_time, '%H:%M').time()


    async def async_set_value(self, value: time) -> None:
        self.start_time = value.strftime('%H:%M')


class ScooperNightModeEndTime(CoordinatorEntity, TimeEntity):
    end_time: str = '23:00'

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_night_mode_end_time')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "scooper_night_mode_end_time"

    @property
    def icon(self) -> str | None:
        return 'mdi:bed-clock'

    @property
    def entity_category(self) -> EntityCategory | None:
        return EntityCategory.CONFIG

    @property
    def native_value(self) -> time | None:
        return datetime.strptime(self.end_time, '%H:%M').time()

    async def async_set_value(self, value: time) -> None:
        self.end_time = value.strftime('%H:%M')


class ScooperQuietModeSwitch(CoordinatorEntity, SwitchEntity):

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }
    @property
    def unique_id(self) -> str:
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_quiet_mode_switch')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "scooper_quiet_mode_switch"

    @property
    def is_on(self) -> bool:
        return self.scooper_data.device_detail['quietEnable']

    @property
    def available(self) -> bool:
        return self.scooper_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        if self.is_on:
            return 'mdi:lock-open-check-outline'
        else:
            return 'mdi:lock-open-minus-outline'

    @property
    def entity_category(self) -> EntityCategory | None:
        return EntityCategory.CONFIG

    async def async_turn_on(self, **kwargs) -> None:
        api = 'token/device/quietMode'
        params = {
            'deviceId': self.scooper_data.id,
            'enable': 1,
            'times': ScooperNightModeStartTime.start_time + '-' + ScooperNightModeEndTime.end_time
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['keyLockStatus'] = True
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

    async def async_turn_off(self, **kwargs) -> None:
        api = 'token/device/quietMode'
        params = {
            'deviceId': self.scooper_data.id,
            'enable': 0
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['quietEnable'] = False
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class ScooperKeyLockSwitch(CoordinatorEntity, SwitchEntity):

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }
    @property
    def unique_id(self) -> str:
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_key_lock_switch')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "scooper_key_lock_switch"

    @property
    def is_on(self) -> bool:
        return self.scooper_data.device_detail['keyLock'] == '01'

    @property
    def available(self) -> bool:
        return self.scooper_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        if self.is_on:
            return 'mdi:lock-check-outline'
        else:
            return 'mdi:lock-open-outline'

    @property
    def entity_category(self) -> EntityCategory | None:
        return EntityCategory.CONFIG

    async def async_turn_on(self, **kwargs) -> None:
        api = 'token/device/keyLock'
        params = {
            'deviceId': self.scooper_data.id,
            'lockStatus': '01',
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['keyLockStatus'] = '01'
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

    async def async_turn_off(self, **kwargs) -> None:
        api = 'token/device/keyLock'
        params = {
            'deviceId': self.scooper_data.id,
            'lockStatus': '00',
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['keyLockStatus'] = '00'
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class ScooperIndicatorSoundSwitch(CoordinatorEntity, SwitchEntity):

    def __init__(self, coordinator, scooper_id):
        super().__init__(coordinator)
        self.scooper_id = scooper_id

    @property
    def scooper_data(self) -> LitterBox:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.litter_boxes[self.scooper_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.scooper_data.id)},
            "name": self.scooper_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.scooper_data.device_attrs['deviceType'],
            "sw_version": f'{self.scooper_data.device_detail["firmwareVersion"]}'
        }
    @property
    def unique_id(self) -> str:
        return (self.scooper_data.device_detail['deviceName']
                + '_' + str(self.scooper_data.id) + '_key_sound_switch')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "scooper_key_sound_switch"

    @property
    def is_on(self) -> bool:
        return self.scooper_data.device_detail['paneltone'] == '01'

    @property
    def available(self) -> bool:
        return self.scooper_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        if self.is_on:
            return 'mdi:volume-high'
        else:
            return 'mdi:volume-mute'

    @property
    def entity_category(self) -> EntityCategory | None:
        return EntityCategory.CONFIG

    async def async_turn_on(self, **kwargs) -> None:
        api = 'token/device/keypadTone'
        params = {
            'deviceId': self.scooper_data.id,
            'kind': '00',
            'panelTone': '01',
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['panelTone'] = '01'
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

    async def async_turn_off(self, **kwargs) -> None:
        api = 'token/device/keypadTone'
        params = {
            'deviceId': self.scooper_data.id,
            'kind': '00',
            'panelTone': '00',
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.scooper_data.device_detail['panelTone'] = '00'
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)