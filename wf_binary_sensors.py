import asyncio
import logging
from typing import Any

from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass
from homeassistant.const import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .data_model import WaterFountain
from .coordinator import CatlinkDevicesCoordinator
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


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
