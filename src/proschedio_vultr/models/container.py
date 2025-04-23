from typing import Literal, TypedDict

class CreateContainerRegistryConfig(TypedDict):
    """
    Data structure used for creating a Vultr Container Registry Subscription.
    """
    name: str
    public: bool
    region: str
    plan: str

class UpdateContainerRegistryConfig(TypedDict, total=False):
    """
    Data structure used for updating a Vultr Container Registry Subscription.
    All fields are optional.
    """
    public: bool | None
    plan: str | None

class UpdateContainerRepositoryConfig(TypedDict):
    """
    Data structure used for updating a Vultr Container Registry Repository.
    """
    description: str

class ContainerRobotAccessConfig(TypedDict):
    action: Literal["pull", "push", "delete"]
    resource: str
    effect: Literal["allow", "deny"]

class UpdateContainerRobotConfig(TypedDict, total=False):
    """
    Data structure used for updating a Vultr Container Registry Robot.
    All fields are optional.
    """
    description: str | None
    disable: bool | None
    duration: int | None
    access: list[ContainerRobotAccessConfig] | None