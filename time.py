import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.components.sensor import (
    DOMAIN as ENTITY_DOMAIN,
)
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .water_fountain_device import *
from .scooper_device import *
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
    time_elem = []

    for ft_id, fountain in coordinator.data.water_fountains.items():
        time_elem.extend((
            WaterFountainNightModeStartTime(coordinator, ft_id),
            WaterFountainNightModeEndTime(coordinator, ft_id)
        ))

    for scooper_id, scooper in coordinator.data.litter_boxes.items():
        time_elem.extend((
            ScooperNightModeStartTime(coordinator, scooper_id),
            ScooperNightModeEndTime(coordinator, scooper_id)
        ))

    async_add_entities(time_elem)
