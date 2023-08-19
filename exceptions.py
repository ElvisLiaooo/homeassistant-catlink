from typing import Any


class CatlinkError(Exception):

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""
        Exception.__init__(self, *args)

class AuthError(Exception):
    """Authentication issue from Catlink api."""

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""
        Exception.__init__(self, *args)

class ServerError(Exception):
    """Catlink server error."""

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""
        Exception.__init__(self, *args)

class NoDevicesError(Exception):
    """ No Devices from Catlink API. """
