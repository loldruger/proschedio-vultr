from typing import TypedDict

class CreateConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Object Storage.
    `cluster_id` is required.
    """
    cluster_id: int # Required
    label: str | None
