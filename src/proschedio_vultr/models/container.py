from typing import Literal, TypedDict

class CreateContainerRegistryBody(TypedDict):
    """
    Data structure used for creating a Vultr Container Registry Subscription.
    """
    name: str
    public: bool
    region: str
    plan: str

class UpdateContainerRegistryBody(TypedDict, total=False):
    """
    Data structure used for updating a Vultr Container Registry Subscription.
    All fields are optional.
    """
    public: bool | None
    plan: str | None

class UpdateContainerRepositoryBody(TypedDict):
    """
    Data structure used for updating a Vultr Container Registry Repository.
    """
    description: str

class ContainerRobotAccess(TypedDict):
    action: Literal["pull", "push", "delete"]
    resource: str
    effect: Literal["allow", "deny"]

class UpdateContainerRobotBody(TypedDict, total=False):
    """
    Data structure used for updating a Vultr Container Registry Robot.
    All fields are optional.
    """
    description: str | None
    disable: bool | None
    duration: int | None
    access: list[ContainerRobotAccess] | None