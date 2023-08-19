import asyncio
import logging
from typing import Any

from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .data_model import WaterFountain
from .const import DOMAIN,WATER_FOUNTAIN_RUN_MODE

_LOGGER = logging.getLogger(__name__)


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

