from typing import Literal, TypedDict

class InstanceCreateConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr VPS Instance.
    """
    os_id: int | None
    ipxe_chain_url: str | None
    iso_id: str | None
    script_id: str | None
    snapshot_id: str | None
    enable_ipv6: bool | None
    disable_public_ipv4: bool | None
    attach_vpc: list[str] | None
    label: str | None
    sshkey_id: list[str] | None
    backups: Literal["enabled", "disabled"] | None
    app_id: int | None
    image_id: str | None
    user_data: str | None
    ddos_protection: bool | None
    activation_email: bool | None
    hostname: str | None
    firewall_group_id: str | None
    reserved_ipv4: str | None
    enable_vpc: bool | None
    tags: list[str] | None
    # Deprecated fields omitted: attach_private_network, attach_vpc2, tag, enable_private_network, enable_vpc2
    # Fields potentially added by user request: user_scheme, app_variables
    user_scheme: Literal["root", "limited"] | None
    # self._app_variables: dict] = None
    wait_for_ready: bool | None
    wait_timeout: int | None
    wait_interval: int | None

class InstanceUpdateConfig(TypedDict, total=False):
    """
    Data structure used for updating a Vultr VPS Instance.
    All fields are optional.
    """
    label: str | None
    user_scheme: Literal["root", "limited"] | None
    enable_ipv6: bool | None
    attach_vpc: list[str] | None
    detach_vpc: list[str] | None
    attach_vpc2: list[str] | None # Deprecated
    detach_vpc2: list[str] | None # Deprecated
    os_id: int | None
    app_id: int | None
    image_id: str | None
    firewall_group_id: str | None
    plan: str | None
    tags: list[str] | None
    backups: Literal["enabled", "disabled"] | None
    hostname: str | None

class InstanceCreateRequestBody(TypedDict):
    """
    Data structure used for creating a Vultr VPS Instance.
    """
    region: str
    plan: str
    os_id: int | None
    ipxe_chain_url: str | None
    iso_id: str | None
    script_id: str | None
    snapshot_id: str | None
    enable_ipv6: bool | None
    disable_public_ipv4: bool | None
    attach_vpc: list[str] | None
    label: str | None
    sshkey_id: list[str] | None
    backups: Literal["enabled", "disabled"] | None
    app_id: int | None
    image_id: str | None
    user_data: str | None
    ddos_protection: bool | None
    activation_email: bool | None
    hostname: str | None
    firewall_group_id: str | None
    reserved_ipv4: str | None
    enable_vpc: bool | None
    tags: list[str] | None
    # Deprecated fields omitted: attach_private_network, attach_vpc2, tag, enable_private_network, enable_vpc2
    # Fields potentially added by user request: user_scheme, app_variables
    user_scheme: Literal["root", "limited"] | None
    # self._app_variables: dict] = None