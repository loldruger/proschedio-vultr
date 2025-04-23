from typing import Literal, TypedDict

class CreateReservedIpConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Reserved IP.
    `region` and `ip_type` are required.
    """
    region: str # Required
    ip_type: Literal["v4", "v6"] # Required
    label: str | None
