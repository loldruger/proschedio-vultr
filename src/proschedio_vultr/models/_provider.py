from typing import Literal, TypedDict

class ProviderConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr VPS Instance.
    """
    os_id: int | None