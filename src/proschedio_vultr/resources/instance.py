from typing import Any
from proschedio_vultr.request import ErrorResponse, Result
from rustipy.option import Nothing
from .resource_base import BaseResource
from ..models import InstanceCreateConfig


class Resource:
    @staticmethod
    def instance(provider: str, region: str, plan: str, config: InstanceCreateConfig) -> 'ResourceInstance':
        return ResourceInstance(provider, region, plan, config)
    
class ResourceInstance(BaseResource):
    def __init__(self, provider: str, region: str, plan: str, config: InstanceCreateConfig):
        self._provider = provider
        self._region = region
        self._plan = plan
        self._config = config

    @property
    def region(self) -> str | None:
        raise NotImplementedError
    
    @property
    def status(self) -> str | None:
        raise NotImplementedError

    @property
    def main_ip(self) -> str | None:
        raise NotImplementedError

    @property
    def provider_specific_data(self) -> dict[str, Any]:
        raise NotImplementedError

    async def create(self) -> Result[BaseResource, ErrorResponse]:
        raise NotImplementedError

    async def delete(self) -> Result[Nothing, ErrorResponse]:
        raise NotImplementedError

    async def update(self) -> Result[BaseResource, ErrorResponse]:
        raise NotImplementedError

    async def get(self) -> Result[BaseResource, ErrorResponse]:
        raise NotImplementedError

    async def list(self) -> Result[list[BaseResource], ErrorResponse]:
        raise NotImplementedError

    async def execute_action(self, action_name: str, **kwargs: Any) -> Result[Any, ErrorResponse]:
        raise NotImplementedError


