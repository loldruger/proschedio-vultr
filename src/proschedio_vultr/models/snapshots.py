from typing import Literal, TypedDict

class CreateSnapshotFromUrlConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Snapshot from a URL.
    `url` is required.
    """
    url: str # Required
    description: str | None
    uefi: Literal["true", "false"] | None