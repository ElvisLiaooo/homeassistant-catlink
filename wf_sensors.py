from typing import Any

from homeassistant.components.sensor import (
    SensorEntity, SensorStateClass, SensorDeviceClass,
)
from homeassistant.const import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .data_model import WaterFountain
from .const import DOMAIN, WATER_FOUNTAIN_RUN_MODE


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
        filtered.sort(key = lambda x: int(x['id']), reverse=True)

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
        last_data = None

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
        filtered.sort(key = lambda x: int(x['id']), reverse=True)

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
        last_data = None

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

    @property
    def device_class(self) -> SensorDeviceClass:
        return SensorDeviceClass.DURATION


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
