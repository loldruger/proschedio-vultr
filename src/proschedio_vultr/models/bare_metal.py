from typing import Literal, TypedDict

class CreateConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Bare Metal instance.
    `region` and `plan` are required.
    """
    region: str # Required
    plan: str # Required
    script_id: str | None
    enable_ipv6: bool | None
    sshkey_id: list[str] | None
    user_data: str | None
    label: str | None
    activation_email: bool | None
    hostname: str | None
    reserved_ipv4: str | None
    os_id: int | None
    snapshot_id: str | None
    app_id: int | None
    image_id: str | None
    persistent_pxe: bool | None
    attach_vpc2: list[str] | None
    detach_vpc2: list[str] | None # Note: detach_vpc2 seems unusual for creation, check API docs if needed. Included for consistency with original class.
    enable_vpc2: bool | None
    tags: list[str] | None
    user_scheme: Literal["root", "limited"] | None
    mdisk_mode: Literal["raid1", "jbod", "none"] | None
    app_variables: dict[str, str] | None

class UpdateBareMetalConfig(TypedDict, total=False):
    """
    Data structure used for updating a Vultr Bare Metal instance.
    All fields are optional.
    """
    user_data: str | None
    label: str | None
    os_id: int | None
    app_id: int | None
    image_id: str | None
    enable_ipv6: bool | None
    attach_vpc2: list[str] | None
    detach_vpc2: list[str] | None
    enable_vpc2: bool | None
    tags: list[str] | None
    user_scheme: Literal["root", "limited"] | None
    mdisk_mode: Literal["raid1", "jbod", "none"] | None

class CreateBareMetalReverseIPv4Body(TypedDict):
    """
    Data structure used for creating a reverse IPv4 entry for a Bare Metal Instance.
    """
    ip: str
    reverse: str

class CreateBareMetalReverseIPv6Body(TypedDict):
    """
    Data structure used for creating a reverse IPv6 entry for a Bare Metal Instance.
    """
    ip: str
    reverse: str