from typing import TypedDict

class CreateConfig(TypedDict, total=False):
    region: str
    description: str | None
    ip_block: str | None
    prefix_length: int | None
