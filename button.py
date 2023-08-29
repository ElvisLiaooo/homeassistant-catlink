import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.components.sensor import (
    DOMAIN as ENTITY_DOMAIN,
)
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .feeder_device import *
from .water_fountain_device import *
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
    buttons = []

    for ft_id, fountain in coordinator.data.water_fountains.items():
        buttons.extend((
            WaterFountainFluffyHair(coordinator, ft_id),

        ))

    for feeder_id, feeder in coordinator.data.feeders.items():
        buttons.extend((
            FeederFoodOutButton(coordinator, feeder_id),
        ))
    async_add_entities(buttons)
