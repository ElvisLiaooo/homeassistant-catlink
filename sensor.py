"""Support for sensor."""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.components.sensor import (
    DOMAIN as ENTITY_DOMAIN,
)
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .water_fountain_device import *
from .feeder_device import *
from .coordinator import CatlinkDevicesCoordinator
from .const import (
    DOMAIN,
    CATLINK_COORDINATOR
)

_LOGGER = logging.getLogger(__name__)

DATA_KEY = f'{ENTITY_DOMAIN}.{DOMAIN}'


async def async_setup_entry(hass: HomeAssistant,
                            entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator: CatlinkDevicesCoordinator = hass.data[DOMAIN][entry.entry_id][CATLINK_COORDINATOR]
    sensors = []

    for ft_id, fountain in coordinator.data.water_fountains.items():
        sensors.extend((
            WaterFountainStatus(coordinator, ft_id),
            WaterFountainWaterLevel(coordinator, ft_id),
            WaterFountainWaterLevelDesc(coordinator, ft_id),
            FilterRemainDays(coordinator, ft_id),
            WaterFountainRunMode(coordinator, ft_id),
            LastDrinkEvent(coordinator, ft_id),
            LastFountainEvent(coordinator, ft_id),
            CatDrinkTotalTimeToday(coordinator, ft_id),
            CatDrinkCountToday(coordinator, ft_id),
        ))

    for feeder_id, feeder in coordinator.data.feeders.items():
        sensors.extend((
            FeederFoodWeight(coordinator, feeder_id),
            FeederFoodOutStatus(coordinator, feeder_id),
            FeederPowerSupplyStatus(coordinator, feeder_id),
            FeederErrorMessage(coordinator, feeder_id),
            FeederAutoFoodOutCount(coordinator, feeder_id),
            FeederDietFoodOutCount(coordinator, feeder_id),
            FeederManualFoodOutCount(coordinator, feeder_id),
            FeederTimingFoodOutCount(coordinator, feeder_id),
            LastEatEvent(coordinator, feeder_id),
            LastFeederEvent(coordinator, feeder_id),
        ))
    async_add_entities(sensors)



