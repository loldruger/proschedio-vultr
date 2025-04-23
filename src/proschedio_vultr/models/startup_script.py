from typing import Literal, TypedDict

class UpdateStartupScriptConfig(TypedDict, total=False):
    """
    Data structure used for updating a Vultr Startup Script.
    All fields are optional.
    """
    name: str | None
    script: str | None # Base64 encoded
    type: Literal["boot", "pxe"] | None
