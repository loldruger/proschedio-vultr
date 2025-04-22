from typing import TypedDict

class CreateConfig(TypedDict, total=False):
    region: str
    description: str | None
    v4_subnet: str | None
    v4_subnet_mask: int | None
