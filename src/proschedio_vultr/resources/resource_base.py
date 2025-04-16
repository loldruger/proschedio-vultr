from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

from rustipy.option import Nothing

from ..request import ErrorResponse, Result

class BaseResource(ABC):
    """
    Abstract base class for resources.
    """

    def __init__(self, provider: str, **kwargs: Any):
        self._provider = provider
        self._id = id
        self._config_kwargs = kwargs
        self._properties: dict[str, Any] = {}
        self._raw_data: dict[str, Any] = {}

    @property
    def id(self) -> Callable[[object], int]:
        return self._id

    @property
    def provider(self) -> str:
        return self._provider
    
    @property
    @abstractmethod
    def status(self) -> str | None:
        pass

    @property
    @abstractmethod
    def region(self) -> str | None:
        pass

    @property
    @abstractmethod
    def main_ip(self) -> str | None:
        pass

    @property
    def provider_specific_data(self) -> dict[str, Any]:
        return {}

    @abstractmethod
    async def create(self) -> 'Result[BaseResource, ErrorResponse]':
        pass

    @abstractmethod
    async def delete(self) -> 'Result[Nothing, ErrorResponse]':
        pass

    @abstractmethod
    async def update(self) -> 'Result[BaseResource, ErrorResponse]':
        pass

    @abstractmethod
    async def get(self) -> 'Result[BaseResource, ErrorResponse]':
        pass

    @abstractmethod
    async def list(self) -> 'Result[list[BaseResource], ErrorResponse]':
        pass

    async def execute_action(self, action_name: str, **kwargs: Any) -> 'Result[Any, ErrorResponse]':
        """
        Executes a provider-specific action.

        Args:
            action_name (str): The name of the action to execute (e.g., 'reinstall', 'set_backup_schedule').
            **kwargs: Parameters required by the specific action.

        Returns:
            Any: The result of the action, if any.

        Raises:
            NotImplementedError: If the action_name is not supported by the provider.
            ValueError: If required kwargs are missing or invalid.
        """
        raise NotImplementedError(f"Action '{action_name}' is not implemented for provider '{self.provider}'")