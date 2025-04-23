from typing import Literal, TypedDict

class CreateSnapshotConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Snapshot.
    `instance_id` is required.
    """
    instance_id: str # Required
    description: str | None

class UpdateSnapshotConfig(TypedDict):
    """
    Data structure used for updating a Vultr Snapshot.
    """
    description: str

class CreateSnapshotFromUrlConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Snapshot from a URL.
    `url` is required.
    """
    url: str # Required
    description: str | None
    uefi: Literal["true", "false"] | None