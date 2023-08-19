"""Config Flow for PetKit integration."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv

from .exceptions import AuthError
from .const import DOMAIN, POLLING_INTERVAL, CONF_PHONE
from .api_validate_util import NoDevicesError, async_validate_api


DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_PHONE): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
    }
)


class CatlinkConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for PetKit integration."""

    VERSION = 1

    entry: config_entries.ConfigEntry | None

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> CatlinkOptionsFlowHandler:
        """Get the options flow for this handler."""
        return CatlinkOptionsFlowHandler(config_entry)

    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult:
        """Handle re-authentication with Catlink."""

        self.entry = self.hass.config_entries.async_get_entry(self.context["entry_id"])
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(
            self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Confirm re-authentication with PetKit."""

        errors: dict[str, str] = {}

        if user_input:
            phone = user_input[CONF_PHONE]
            password = user_input[CONF_PASSWORD]

            try:
                await async_validate_api(self.hass, phone, password)
            except AuthError:
                errors["base"] = "invalid_auth"
            except ConnectionError:
                errors["base"] = "cannot_connect"
            except NoDevicesError:
                errors["base"] = "no_devices"
            else:
                assert self.entry is not None

                self.hass.config_entries.async_update_entry(
                    self.entry,
                    data={
                        **self.entry.data,
                        CONF_PHONE: phone,
                        CONF_PASSWORD: password,
                    },
                    options={
                        POLLING_INTERVAL: self.entry.options[POLLING_INTERVAL],
                    }
                )

                await self.hass.config_entries.async_reload(self.entry.entry_id)
                return self.async_abort(reason="reauth_successful")

        return self.async_show_form(
            step_id="reauth_confirm",
            data_schema=DATA_SCHEMA,
            errors=errors,
        )

    async def async_step_user(
            self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""


        errors: dict[str, str] = {}

        if user_input:
            phone = user_input[CONF_PHONE]
            password = user_input[CONF_PASSWORD]

            try:
                await async_validate_api(self.hass, phone, password)
            except AuthError:
                errors["base"] = "invalid_auth"
            except ConnectionError:
                errors["base"] = "cannot_connect"
            except NoDevicesError:
                errors["base"] = "no_devices"
            else:
                await self.async_set_unique_id(phone)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title="Catlink",
                    data={
                        CONF_PHONE: phone,
                        CONF_PASSWORD: password
                    },
                    options={
                        POLLING_INTERVAL: 10,
                    }
                )

        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors,
        )


class CatlinkOptionsFlowHandler(config_entries.OptionsFlow):
    """ Handle PetKit integration options. """

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """ Manage options. """
        return await self.async_step_catlink_options()

    async def async_step_catlink_options(self, user_input=None):
        """Manage the PetKit options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options = {
            vol.Required(
                POLLING_INTERVAL,
                default=self.config_entry.options.get(
                    POLLING_INTERVAL, 120
                ),
            ): int,
        }

        return self.async_show_form(step_id="catlink_options", data_schema=vol.Schema(options))
