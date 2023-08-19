import asyncio
import logging
from typing import Any

from homeassistant.components.select import SelectEntity
from homeassistant.const import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .data_model import WaterFountain
from .const import DOMAIN,WATER_FOUNTAIN_RUN_MODE

_LOGGER = logging.getLogger(__name__)
WATER_FOUNTAIN_RUN_MODE_OPTION_MAPPING = {v: k for k, v in WATER_FOUNTAIN_RUN_MODE.items()}


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

