import os
import json
from http import HTTPMethod
from typing import Any
from rustipy.result import Result, Ok, Err
from rustipy.option import Nothing
from .resource_base import BaseResource, ResourceState
from ..models import InstanceCreateConfig
from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import URL_INSTANCES, URL_INSTANCE

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

    @staticmethod
    async def create(config: dict[str, Any]) -> Result[ResourceState, ErrorResponse]:
        """Creates a new Vultr instance."""
        url = URL_INSTANCES.to_str()
        result = await (
            Request(url)
            .set_method(HTTPMethod.POST)
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
            .add_header("Content-Type", "application/json")
            .set_body(json.dumps(config))
            .request()
        )

        if result.is_ok():
            return Err(ErrorResponse(status_code=501, error="Mapping from API response to ResourceState not implemented"))
        else:
            return Err(result.err_value)

    @staticmethod
    async def get(resource_id: str) -> Result[ResourceState, ErrorResponse]:
        """Gets a specific Vultr instance."""
        url = URL_INSTANCE.assign("instance-id", resource_id).to_str()
        result = await (
            Request(url)
            .set_method(HTTPMethod.GET)
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
            .request()
        )

        if result.is_ok():
            return Err(ErrorResponse(status_code=501, error="Mapping from API response to ResourceState not implemented"))
        else:
            return Err(result.err_value)

    @staticmethod
    async def update(resource_id: str, config: dict[str, Any]) -> Result[ResourceState, ErrorResponse]:
        """Updates an existing Vultr instance."""
        url = URL_INSTANCE.assign("instance-id", resource_id).to_str()
        result = await (
            Request(url)
            .set_method(HTTPMethod.PATCH)
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
            .add_header("Content-Type", "application/json")
            .set_body(json.dumps(config))
            .request()
        )

        if result.is_ok():
            return Err(ErrorResponse(status_code=501, error="Mapping from API response to ResourceState not implemented"))
        else:
            return Err(result.err_value)

    @staticmethod
    async def delete(resource_id: str) -> Result[Nothing, ErrorResponse]:
        """Deletes a Vultr instance."""
        url = URL_INSTANCE.assign("instance-id", resource_id).to_str()
        result = await (
            Request(url)
            .set_method(HTTPMethod.DELETE)
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
            .request()
        )

        if result.is_ok():
            return Ok(None)
        else:
            return Err(result.err_value)

    @staticmethod
    async def list(filters: dict[str, Any] | None = None) -> Result[list[ResourceState], ErrorResponse]:
        """Lists Vultr instances, optionally applying filters."""
        url = URL_INSTANCES.to_str()
        request = (
            Request(url)
            .set_method(HTTPMethod.GET)
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )

        if filters is not None:
            for key, value in filters.items():
                request.add_param(key, value)

        result = await request.request()

        if result.is_ok():
            return Err(ErrorResponse(status_code=501, error="Mapping from API response list to list[ResourceState] not implemented"))
        else:
            return Err(result.err_value)

    async def execute_action(self, action_name: str, **kwargs: Any) -> Result[Any, ErrorResponse]:
        raise NotImplementedError("Actions should be handled by the specific handler (e.g., ServerInstanceHandler)")


