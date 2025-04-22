from typing import TypedDict

class CreateConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr VFS subscription.

    Args:
        region (str): Region identifier where to create the VFS.
        label (str): User-defined label for the VFS subscription.
        storage_size (int): Size in gigabytes for the VFS.
    """
    region: str
    label: str
    storage_size: int
    disk_type: str | None
    tags: list[str] | None

class UpdateConfig(TypedDict, total=False):
    label: str
    storage_size: int
