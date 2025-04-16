import logging
from typing import Any

# Import the interface definition
from .plugin import Plugin, ResourceState, ActionResult, ErrorDetails
# Import Result type
from rustipy.result import Result, Ok, Err
# Import specific {self.provider}logic handlers (you'll need to create/refactor these)
from .resources import instance as instance_resource
from .actions import instance as instance_action
# Hypothetical API client for Vultr
from .request import VultrApiClient, ErrorResponse # Assuming ErrorResponse can be adapted to ErrorDetails

logger = logging.getLogger(__name__)

class VultrPlugin(Plugin):
    provider_name = "vultr"

    def __init__(self):
        self._api_client: VultrApiClient | None = None
        # Map generic resource types to Vultr-specific handler modules/classes
        self._resource_managers = {
            "server_instance": instance_resource,
            # "database": database_resource, # Example for other resources
        }
        # Map generic action names to Vultr-specific functions/methods
        self._action_executors = {
            # Resource lifecycle actions mapped to resource methods
            "CreateServerInstance": self._proxy_create_resource,
            "UpdateServerInstance": self._proxy_update_resource,
            "DeleteServerInstance": self._proxy_delete_resource,
            # Operational actions mapped to action handlers
            "StartInstance": instance_action.start_instance, # Assuming these exist
            "StopInstance": instance_action.stop_instance,
            "RebootInstance": instance_action.reboot_instance,
            "ReinstallInstance": instance_action.reinstall_instance,
            "AttachIsoToInstance": instance_action.attach_instance_iso,
            # ... map other actions from your actions/instance.py ...
        }

    def _to_error_details(self, error_response: ErrorResponse) -> ErrorDetails:
        # Convert provider-specific ErrorResponse to the standard ErrorDetails dict
        return {
            "status_code": error_response.status_code,
            "error_code": error_response.error_code,
            "message": error_response.message,
            "details": error_response.details
        }

    async def initialize(self, credentials: dict[str, Any]) -> Result[None, ErrorDetails]:
        api_key = credentials.get("api_key") # Expecting specific key name
        if api_key is None:
            return Err({"error_code": "MISSING_CREDENTIALS", "message": f"{self.provider_name} API key ('api_key') is required."})
        try:
            self._api_client = VultrApiClient(api_key)
            # You might want to test the connection here
            logger.info(f"{self.provider_name} plugin initialized successfully.")
            return Ok(None)
        except Exception as e:
             logger.error(f"Failed to initialize {self.provider_name} plugin: {e}", exc_info=True)
             return Err({"error_code": "INITIALIZATION_FAILED", "message": str(e)})

    # --- Resource Interface Implementation ---

    async def create(self, resource_type: str, config: dict[str, Any]) -> Result[ResourceState, ErrorDetails]:
        if self._api_client is None: return Err({"error_code": "NOT_INITIALIZED", "message": "Plugin not initialized."})
        manager = self._resource_managers.get(resource_type)
        if manager is None: return Err({"error_code": "UNSUPPORTED_RESOURCE", "message": f"Resource type '{resource_type}' not supported by {self.provider_name} plugin."})

        # Assuming manager has a 'create' async method taking client and config
        # The create method should return Result[ResourceState, ErrorResponse]
        result = await manager.create(self._api_client, config)
        return result.map_err(self._to_error_details)

    async def get(self, resource_type: str, resource_id: str) -> Result[ResourceState, ErrorDetails]:
        if self._api_client is None: return Err({"error_code": "NOT_INITIALIZED", "message": "Plugin not initialized."})
        manager = self._resource_managers.get(resource_type)
        if manager is None: return Err({"error_code": "UNSUPPORTED_RESOURCE", "message": f"Resource type '{resource_type}' not supported."})

        # Assuming manager has a 'get' async method
        result = await manager.get(self._api_client, resource_id)
        return result.map_err(self._to_error_details)

    async def update(self, resource_type: str, resource_id: str, config: dict[str, Any]) -> Result[ResourceState, ErrorDetails]:
        if self._api_client is None: return Err({"error_code": "NOT_INITIALIZED", "message": "Plugin not initialized."})
        manager = self._resource_managers.get(resource_type)
        if manager is None: return Err({"error_code": "UNSUPPORTED_RESOURCE", "message": f"Resource type '{resource_type}' not supported."})

        # Assuming manager has an 'update' async method
        result = await manager.update(self._api_client, resource_id, config)
        return result.map_err(self._to_error_details)

    async def delete(self, resource_type: str, resource_id: str) -> Result[None, ErrorDetails]:
        if self._api_client is None: return Err({"error_code": "NOT_INITIALIZED", "message": "Plugin not initialized."})
        manager = self._resource_managers.get(resource_type)
        if manager is None: return Err({"error_code": "UNSUPPORTED_RESOURCE", "message": f"Resource type '{resource_type}' not supported."})

        # Assuming manager has a 'delete' async method
        result = await manager.delete(self._api_client, resource_id)
        # map_err works for Result[None, Error] as well
        return result.map_err(self._to_error_details)

    async def list(self, resource_type: str, filters: dict[str, Any] | None = None) -> Result[list[ResourceState], ErrorDetails]:
        if self._api_client is None: return Err({"error_code": "NOT_INITIALIZED", "message": "Plugin not initialized."})
        manager = self._resource_managers.get(resource_type)
        if manager is None: return Err({"error_code": "UNSUPPORTED_RESOURCE", "message": f"Resource type '{resource_type}' not supported."})

        # Assuming manager has a 'list' async method
        result = await manager.list(self._api_client, filters)
        return result.map_err(self._to_error_details)

    # --- Action Interface Implementation ---

    async def execute(self, action_name: str, parameters: dict[str, Any]) -> Result[ActionResult, ErrorDetails]:
        if self._api_client is None: return Err({"error_code": "NOT_INITIALIZED", "message": "Plugin not initialized."})

        executor = self._action_executors.get(action_name)
        if executor is None:
            return Err({"error_code": "UNSUPPORTED_ACTION", "message": f"Action '{action_name}' not supported by {self.provider_name}plugin."})

        try:
            # Pass the API client and unpack parameters into the executor function
            # The executor function should return Result[ActionResult, ErrorResponse]
            result = await executor(self._api_client, **parameters)
            # Map potential ErrorResponse to standard ErrorDetails
            return result.map_err(self._to_error_details)
        except TypeError as e:
             logger.error(f"Type error executing action '{action_name}' with params {parameters}: {e}", exc_info=True)
             return Err({"error_code": "INVALID_PARAMETERS", "message": f"Invalid parameters for action '{action_name}': {e}"})
        except Exception as e:
            logger.error(f"Error executing action '{action_name}': {e}", exc_info=True)
            return Err({"error_code": "ACTION_EXECUTION_FAILED", "message": str(e)})

    async def list_actions(self, resource_type: str | None = None) -> Result[list[str], ErrorDetails]:
        # Basic implementation: return all known action names
        # TODO: Implement filtering based on resource_type if needed
        if resource_type is not None:
            logger.warning(f"Filtering actions by resource_type is not yet implemented in {self.provider_name} plugin.")
        return Ok(list(self._action_executors.keys()))

    # --- Proxy methods to handle actions that map to resource lifecycle ---
    # These methods adapt the resource calls to the action interface

    async def _proxy_create(self, client: VultrApiClient, **parameters: Any) -> Result[ActionResult, ErrorResponse]:
        resource_type = parameters.get("resource_type")
        config = parameters.get("config")
        if resource_type is None or config is None:
            return Err(ErrorResponse(status_code=400, error_code="INVALID_PARAMETERS", message="'resource_type' and 'config' are required for Create action."))
        # Call the actual resource creation method
        create_result = await self.create(resource_type, config)
        # Map the result: ResourceState becomes ActionResult
        return create_result.map(lambda state: state) # Simple mapping for now

    async def _proxy_update(self, client: VultrApiClient, **parameters: Any) -> Result[ActionResult, ErrorResponse]:
        resource_type = parameters.get("resource_type")
        resource_id = parameters.get("resource_id")
        config = parameters.get("config")
        if resource_type is None or resource_id is None or config is None:
             return Err(ErrorResponse(status_code=400, error_code="INVALID_PARAMETERS", message="'resource_type', 'resource_id', and 'config' are required for Update action."))
        update_result = await self.update(resource_type, resource_id, config)
        return update_result.map(lambda state: state)

    async def _proxy_delete(self, client: VultrApiClient, **parameters: Any) -> Result[ActionResult, ErrorResponse]:
        resource_type = parameters.get("resource_type")
        resource_id = parameters.get("resource_id")
        if resource_type is None or resource_id is None:
             return Err(ErrorResponse(status_code=400, error_code="INVALID_PARAMETERS", message="'resource_type' and 'resource_id' are required for Delete action."))
        delete_result = await self.delete(resource_type, resource_id)
        # If successful (None), return an empty dict for ActionResult
        return delete_result.map(lambda _: {})