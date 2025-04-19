from abc import ABC, abstractmethod
from typing import Any
from rustipy.option import Nothing
from rustipy.result import Result
from ..plugin import ResourceState, ActionResult, ErrorDetails
# from ..request import VultrApiClient # Assuming the client is passed

class ResourceHandlerInterface(ABC):
    """Interface for handling a specific resource type."""

    # Remove client dependency from __init__
    def __init__(self):
        # self._client = client # Removed
        pass

    @abstractmethod
    async def create(self, config: dict[str, Any]) -> Result[ResourceState, ErrorDetails]:
        pass

    @abstractmethod
    async def get(self, resource_id: str) -> Result[ResourceState, ErrorDetails]:
        pass

    @abstractmethod
    async def update(self, resource_id: str, config: dict[str, Any]) -> Result[ResourceState, ErrorDetails]:
        pass

    @abstractmethod
    async def delete(self, resource_id: str) -> Result[Nothing, ErrorDetails]:
        pass

    @abstractmethod
    async def list(self, filters: dict[str, Any] | None) -> Result[list[ResourceState], ErrorDetails]:
        pass

    @abstractmethod
    async def execute(self, action_name: str, parameters: dict[str, Any]) -> Result[ActionResult, ErrorDetails]:
        """Handles actions specific to this resource type."""
        pass

    @abstractmethod
    async def list_actions(self) -> Result[list[str], ErrorDetails]:
        """Lists actions supported by this handler."""
        pass