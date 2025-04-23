from typing import Literal, TypedDict

class CreateReservedIpConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Reserved IP.
    `region` and `ip_type` are required.
    """
    region: str # Required
    ip_type: Literal["v4", "v6"] # Required
    label: str | None

class UpdateReservedIpConfig(TypedDict):
    """
    Data structure used for updating a Vultr Reserved IP.
    """
    label: str

class ConvertIpToReservedIpConfig(TypedDict, total=False):
    """
    Data structure used for converting an existing instance IP address to a Reserved IP.
    `ip_address` is required.
    """
    ip_address: str # Required
    label: str | None