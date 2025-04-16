from abc import ABC, abstractmethod
from typing import Any, TypeAlias

from rustipy.result import Result

# Define common types for clarity
ResourceState: TypeAlias = dict[str, Any]  # Represents the state of a resource
ActionResult: TypeAlias = dict[str, Any]   # Represents the result of an action
ErrorDetails: TypeAlias = dict[str, Any]   # Standardized error structure

class ResourcePluginInterface(ABC):
    """Interface for managing resource lifecycle."""

    @abstractmethod
    async def create(self, resource_type: str, config: dict[str, Any]) -> Result[ResourceState, ErrorDetails]:
        """Creates a new resource based on the config."""
        pass

    @abstractmethod
    async def get(self, resource_type: str, resource_id: str) -> Result[ResourceState, ErrorDetails]:
        """Gets the current state of a specific resource."""
        pass

    @abstractmethod
    async def update(self, resource_type: str, resource_id: str, config: dict[str, Any]) -> Result[ResourceState, ErrorDetails]:
        """Updates an existing resource according to the config."""
        pass

    @abstractmethod
    async def delete(self, resource_type: str, resource_id: str) -> Result[None, ErrorDetails]:
        """Deletes a specific resource."""
        pass

    @abstractmethod
    async def list(self, resource_type: str, filters: dict[str, Any] | None = None) -> Result[list[ResourceState], ErrorDetails]:
        """Lists resources of a specific type, optionally filtered."""
        pass

class ActionPluginInterface(ABC):
    """Interface for executing actions."""

    @abstractmethod
    async def execute(self, action_name: str, parameters: dict[str, Any]) -> Result[ActionResult, ErrorDetails]:
        """
        Executes a named action with given parameters.
        This can include actions that operate on existing resources
        or actions that result in the creation of new resources.
        """
        pass

    @abstractmethod
    async def list_actions(self, resource_type: str | None = None) -> Result[list[str], ErrorDetails]:
        """Lists actions supported by this plugin, optionally filtered by resource type."""
        # Optional, but useful for discovery
        pass

class Plugin(ResourcePluginInterface, ActionPluginInterface):
    """
    Abstract base class for a complete plugin, combining resource and action interfaces.
    """
    provider_name: str # e.g., "vultr", "aws"

    @abstractmethod
    async def initialize(self, credentials: dict[str, Any]) -> Result[None, ErrorDetails]:
        """Initializes the plugin with necessary credentials and setup."""
        pass