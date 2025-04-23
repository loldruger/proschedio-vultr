from typing import Literal, TypedDict

class CreateUserConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr User.
    `email`, `name`, and `password` are required.
    """
    email: str # Required
    name: str # Required
    password: str # Required
    api_enabled: bool | None
    acls: list[Literal[
        "abuse",
        "alerts",
        "billing",
        "dns",
        "firewall",
        "loadbalancer",
        "manage_users",
        "objstore",
        "provisioning",
        "subscriptions",
        "subscriptions_view",
        "support",
        "upgrade",
    ]] | None

class UpdateUserConfig(TypedDict, total=False):
    """
    Data structure used for updating a Vultr User.
    All fields are optional.
    """
    email: str | None
    name: str | None
    password: str | None
    api_enabled: bool | None
    acls: list[Literal[
        "abuse",
        "alerts",
        "billing",
        "dns",
        "firewall",
        "loadbalancer",
        "manage_users",
        "objstore",
        "provisioning",
        "subscriptions",
        "subscriptions_view",
        "support",
        "upgrade",
    ]] | None
