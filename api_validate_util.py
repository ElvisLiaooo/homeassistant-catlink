"""Utilities for PetKit Integration"""
from __future__ import annotations

import logging
import async_timeout

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .catlink_client import CatlinkClient
from .const import TIMEOUT

_LOGGER = logging.getLogger(__name__)


async def async_validate_api(hass: HomeAssistant, phone: str, password: str) -> bool:
    """Get data from API."""

    client = CatlinkClient(
        phone,
        password,
        session=async_get_clientsession(hass),
        timeout=TIMEOUT,
    )

    async with async_timeout.timeout(TIMEOUT):
        await client.async_login(hass)
        devices_query = await client.get_devices(hass)

    if not devices_query:
        _LOGGER.error("Could not retrieve any devices from Catlink servers")
        raise NoDevicesError
    return True


class NoDevicesError(Exception):
    """ No Devices from PetKit API. """
