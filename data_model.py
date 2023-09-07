from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class CatlinkData:
        uid: str
        feeders: Optional[dict[int, Any]] = None
        litter_boxes:  Optional[dict[int, Any]] = None
        water_fountains: Optional[dict[int, Any]] = None
        pets: Optional[dict[int, Any]] = None


@dataclass
class Feeder:
    """Dataclass for Catlink Feeders."""
    id: int
    device_attrs: dict[str, Any]
    device_detail: dict[str, Any]
    event_record: dict[str, Any]
    wifi_info: dict[str, Any]
    type: str


@dataclass
class LitterBox:
    """Dataclass for Catlink Litter Boxes."""
    id: int
    device_attrs: dict[str, Any]
    device_detail: dict[str, Any]
    event_record: dict[str, Any]
    wifi_info: dict[str, Any]
    type: str


@dataclass
class WaterFountain:
    """Dataclass for Catlink Feeders."""
    id: int
    device_attrs: dict[str, Any]
    device_detail: dict[str, Any]
    event_record: list[dict[str, Any]]
    wifi_info: dict[str, Any]
    cat_data: dict[str, Any]
    device_type: str
