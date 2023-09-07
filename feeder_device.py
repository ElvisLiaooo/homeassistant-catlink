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

from .data_model import Feeder
from .const import *
from .coordinator import CatlinkDevicesCoordinator

_LOGGER = logging.getLogger(__name__)


class FeederFoodWeight(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + 'food_weight')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_food_weight"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.feeder_data.device_detail['weight']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:weight'

    @property
    def device_class(self) -> SensorDeviceClass | None:
        return SensorDeviceClass.WEIGHT

    @property
    def native_unit_of_measurement(self) -> str | None:
        return 'g'


class FeederFoodOutStatus(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + 'food_out_status')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_food_out_status"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.feeder_data.device_detail['foodOutStatus']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:food-fork-drink'


class FeederPowerSupplyStatus(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_power_supply_status')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_power_supply_status"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.feeder_data.device_detail['powerSupplyStatus']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:power-plug-battery'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class FeederErrorMessage(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_error_message')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_error_message"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return (self.feeder_data.device_detail['currentErrorType']
                + ': ' + self.feeder_data.device_detail['currentErrorMessage'])

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:alert-circle-outline'

    @property
    def entity_category(self) -> EntityCategory | None:
        return EntityCategory.DIAGNOSTIC


class FeederManualFoodOutCount(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_manual_out_count')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_manual_out_count"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.feeder_data.device_detail['manualFoodOutNum']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:braille'


class FeederTimingFoodOutCount(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_timing_out_count')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_timing_out_count"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.feeder_data.device_detail['timingFoodOutNum']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:clock-alert-outline'


class FeederAutoFoodOutCount(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_auto_out_count')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_auto_out_count"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.feeder_data.device_detail['autoFoodOutNum']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:auto-mode'


class FeederDietFoodOutCount(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_diet_out_count')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_diet_out_count"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.feeder_data.device_detail['dietFoodOutNum']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:food-drumstick-off-outline'


class LastEatEvent(CoordinatorEntity, SensorEntity):
    """Representation of water fountain status."""

    last_data: str = "Unknown"

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_last_eat_event')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_last_eat_event"

    @property
    def native_value(self) -> str | None:
        logs = self.feeder_data.event_record
        if not logs:
            return self.last_data
        filtered = list(filter(lambda x: x['type'] == 'EAT', logs))
        if not filtered:
            return self.last_data
        filtered.sort(key=lambda x: int(x['id']), reverse=True)

        result = filtered[0]
        self.last_data = result['time'] + ', ' + result['firstSection'] + ', ' + result['secondSection']
        return self.last_data

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:food-outline'


class LastFeederEvent(CoordinatorEntity, SensorEntity):
    """Representation of water fountain status."""

    last_data: str = "Unknown"

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_last_feeder_event')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_last_feeder_event"

    @property
    def native_value(self) -> str | None:
        logs = self.feeder_data.event_record
        if not logs:
            return self.last_data
        filtered = list(filter(lambda x: x['type'] != 'EAT', logs))
        if not filtered:
            return self.last_data
        filtered.sort(key=lambda x: int(x['id']), reverse=True)

        result = filtered[0]
        self.last_data = ', '.join((result['time'], result['event'], result['firstSection'], result['secondSection']))
        return self.last_data

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:information-box-outline'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class FeederWifiStatus(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_wifi_status')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_wifi_status"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.feeder_data.wifi_info['wifiStatus']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:wifi'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class FeederWifiStrength(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""
    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_wifi_strength')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_wifi_strength"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.feeder_data.wifi_info['wifiSignalPercent']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:wifi'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class FeederWifiRssi(CoordinatorEntity, SensorEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_wifi_rssi')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_wifi_rssi"

    @property
    def native_value(self) -> str | None:
        """Return status of the feeder."""
        return self.feeder_data.wifi_info['rssi']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:wifi'

    @property
    def entity_category(self) -> EntityCategory:
        """Set category to diagnostic."""
        return EntityCategory.DIAGNOSTIC


class FeederManualFoodOutNumSelect(CoordinatorEntity, SelectEntity):
    """Representation of feeder status."""
    food_out_num: int = 1
    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_manual_food_out_num')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_manual_food_out_num"

    @property
    def available(self) -> bool:
        return self.feeder_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:bowl-mix'

    @property
    def current_option(self) -> str:
        return str(self.food_out_num)

    @property
    def options(self) -> list[str]:
        return list(map(str, range(1,11)))

    async def async_select_option(self, option: str) -> None:
        self.food_out_num = int(option)
        self.async_write_ha_state()
        await self.coordinator.async_request_refresh()


class FeederFoodOutButton(CoordinatorEntity, ButtonEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_food_out_button')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_food_out_button"

    @property
    def available(self) -> bool:
        return self.feeder_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        """Set status icon."""
        return 'mdi:bowl-mix'

    async def async_press(self) -> None:
        api = 'token/device/feeder/foodOut'
        params = {
            'deviceId': self.feeder_data.id,
            'footOutNum': FeederManualFoodOutNumSelect.food_out_num
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class FeederAutoFillFoodSwitch(CoordinatorEntity, SwitchEntity):

    def __init__(self, coordinator: CatlinkDevicesCoordinator, fountain_id):
        super().__init__(coordinator)
        self.feeder_id = fountain_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_auto_fill_food_switch')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "feeder_auto_fill_food_switch"

    @property
    def is_on(self) -> bool:
        return self.feeder_data.device_detail['newAutoFillStatus']

    @property
    def available(self) -> bool:
        return self.feeder_data.device_detail['online']

    @property
    def icon(self) -> str | None:
        return 'mdi:auto-mode'

    @property
    def entity_category(self) -> EntityCategory | None:
        return EntityCategory.CONFIG

    async def async_turn_on(self, **kwargs) -> None:
        api = 'token/device/feeder/newAutoFillFood'
        params = {
            'deviceId': self.feeder_data.id,
            'enable': 1
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.feeder_data.device_detail['newAutoFillStatus'] = True
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

    async def async_turn_off(self, **kwargs) -> None:
        api = 'token/device/feeder/newAutoFillFood'
        params = {
            'deviceId': self.feeder_data.id,
            'enable': 0
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.feeder_data.device_detail['newAutoFillStatus'] = False
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

class FeederLockSwitch(CoordinatorEntity, SwitchEntity):

    def __init__(self, coordinator: CatlinkDevicesCoordinator, fountain_id):
        super().__init__(coordinator)
        self.feeder_id = fountain_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_food_lock_switch')

    @property
    def has_entity_name(self) -> bool:
        return True

    @property
    def translation_key(self) -> str:
        return "feeder_food_lock_switch"

    @property
    def is_on(self) -> bool:
        return self.feeder_data.device_detail['keyLockStatus']

    @property
    def available(self) -> bool:
        return self.feeder_data.device_detail['online']

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
        api = 'token/device/feeder/keyLock/setting'
        params = {
            'deviceId': self.feeder_data.id,
            'lockStatus': 1
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.feeder_data.device_detail['keyLockStatus'] = True
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

    async def async_turn_off(self, **kwargs) -> None:
        api = 'token/device/feeder/keyLock/setting'
        params = {
            'deviceId': self.feeder_data.id,
            'lockStatus': 0
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.feeder_data.device_detail['keyLockStatus'] = False
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)


class FeederIndicatorLightSelect(CoordinatorEntity, SelectEntity):
    """Representation of feeder status."""

    def __init__(self, coordinator, feeder_id):
        super().__init__(coordinator)
        self.feeder_id = feeder_id

    @property
    def feeder_data(self) -> Feeder:
        """Handle coordinator Feeder data."""
        return self.coordinator.data.feeders[self.feeder_id]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device registry information for this entity."""
        return {
            "identifiers": {(DOMAIN, self.feeder_data.id)},
            "name": self.feeder_data.device_detail['deviceName'],
            "manufacturer": "Catlink",
            "model": self.feeder_data.device_attrs['deviceType'],
            "sw_version": f'{self.feeder_data.device_detail["firmwareVersion"]}'
        }

    @property
    def unique_id(self) -> str:
        """Sets unique ID for this entity."""
        return (self.feeder_data.device_detail['deviceName']
                + '_' + str(self.feeder_data.id) + '_indicator_light_select')

    @property
    def has_entity_name(self) -> bool:
        """Indicate that entity has name defined."""
        return True

    @property
    def translation_key(self) -> str:
        """Translation key for this entity."""
        return "feeder_indicator_light_select"

    @property
    def available(self) -> bool:
        return self.feeder_data.device_detail['online']

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
        current_mode = self.feeder_data.device_detail['indicatorLightStatus']
        return FEEDER_LIGHT_MODE[current_mode]

    @property
    def options(self) -> list[str]:
        return list(FEEDER_LIGHT_MODE.values())

    async def async_select_option(self, option: str) -> None:
        api = 'token/device/feeder/light/indicator/setting'
        selected_mode = FEEDER_LIGHT_MODE_OPTIONS[option]
        params = {
            'deviceId': self.feeder_data.id,
            'status': selected_mode,
        }
        resp = await self.coordinator.client.request(api, params, 'POST')
        if resp['success'] and resp['returnCode'] == 0:
            self.feeder_data.device_detail['indicatorLightStatus'] = FEEDER_LIGHT_MODE_OPTIONS_REV[selected_mode]
            self.async_write_ha_state()
            await asyncio.sleep(5)
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.warning('Request api %s with %s failed, Resp %s', api, params, resp)

