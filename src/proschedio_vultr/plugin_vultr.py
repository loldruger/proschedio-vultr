import logging
import os # Import os module
from typing import Any

# Import the interface definition
from .plugin import Plugin, ResourceState, ActionResult, ErrorDetails
# Import Result type
from rustipy.result import Result, Ok, Err
# Import the base handler interface and specific handlers
from .handlers._base_handler import ResourceHandlerInterface # Import base interface
from .handlers.instance_handler import ServerInstanceHandler # Import the concrete handler
# from .handlers.bare_metal_handler import BareMetalHandler # Example
# from .handlers.block_storage_handler import BlockStorageHandler # Example
# Hypothetical API client for Vultr - REMOVED VultrApiClient import
from .request import ErrorResponse # Assuming ErrorResponse can be adapted to ErrorDetails

logger = logging.getLogger(__name__)

class VultrPlugin(Plugin):
    provider_name = "vultr"

    def __init__(self):
        # REMOVED self._api_client initialization
        # Map resource type strings to Handler CLASSES
        self._handler_classes: dict[str, type[ResourceHandlerInterface]] = {
             # Use the imported ServerInstanceHandler class
            "server_instance": ServerInstanceHandler,
            # "bare_metal": BareMetalHandler, # Example for others
            "block_storage": BlockStorageHandler,
            # ... add other resource types and their handler classes
        }
        # Store handler INSTANCES after initialization
        self._handlers: dict[str, ResourceHandlerInterface] = {}

    def _to_error_details(self, error_response: ErrorResponse) -> ErrorDetails:
        # Convert provider-specific ErrorResponse to the standard ErrorDetails dict
        # Assuming ErrorResponse has 'status_code', 'error' attributes
        # If ErrorResponse structure is different, adjust this mapping
        # Example: If it has 'message' instead of 'error'
        # return {
        #     "status_code": error_response.status_code,
        #     "error_code": getattr(error_response, 'error_code', 'UNKNOWN'), # Add error_code if available
        #     "message": getattr(error_response, 'message', str(error_response)), # Use message or fallback
        #     "details": getattr(error_response, 'details', None) # Add details if available
        # }
        # Using the structure from request.py ErrorResponse (status_code, error)
        return {
            "status_code": error_response.get("status_code", 0),
            "error_code": "PROVIDER_ERROR", # Generic code, ErrorResponse has no code field
            "message": error_response.get("error", "Unknown provider error"),
            "details": None # ErrorResponse has no details field
        }

    # Modify initialize to instantiate handlers without client
    async def initialize(self, credentials: dict[str, Any]) -> Result[None, ErrorDetails]:
        # API key is no longer directly used by the plugin class itself
        # but might be needed by the underlying functions (via os.environ)
        # We might still want to check if the key exists for early failure
        api_key = os.environ.get('VULTR_API_KEY') # Or get from credentials if preferred
        if not api_key:
             # Decide if missing key is an initialization error or handled later
             logger.warning(f"{self.provider_name} API key ('VULTR_API_KEY' env var) not found. API calls may fail.")
             # Optionally return Err here if key is strictly required upfront
             # return Err({"error_code": "MISSING_CREDENTIALS", "message": f"{self.provider_name} API key ('VULTR_API_KEY' env var) is required."})

        try:
            # Instantiate all handlers (they don't take client anymore)
            self._handlers = {
                res_type: handler_cls() # Instantiate without arguments
                for res_type, handler_cls in self._handler_classes.items()
            }
            logger.info(f"{self.provider_name} plugin initialized successfully with {len(self._handlers)} handlers.")
            return Ok(None)
        except Exception as e:
             logger.error(f"Failed to initialize {self.provider_name} plugin handlers: {e}", exc_info=True)
             self._handlers = {}
             return Err({"error_code": "INITIALIZATION_FAILED", "message": str(e)})

    # --- Resource Interface Implementation ---

    async def create(self, resource_type: str, config: dict[str, Any]) -> Result[ResourceState, ErrorDetails]:
        # REMOVED self._api_client check
        manager = self._handlers.get(resource_type)
        if manager is None: return Err({"error_code": "UNSUPPORTED_RESOURCE", "message": f"Resource type '{resource_type}' not supported by {self.provider_name} plugin."})

        # Assuming manager has a 'create' async method taking ONLY config
        # The create method should return Result[ResourceState, ErrorResponse]
        # REMOVED passing self._api_client
        result = await manager.create(config)
        return result.map_err(self._to_error_details)

    async def get(self, resource_type: str, resource_id: str) -> Result[ResourceState, ErrorDetails]:
        # REMOVED self._api_client check
        manager = self._handlers.get(resource_type)
        if manager is None: return Err({"error_code": "UNSUPPORTED_RESOURCE", "message": f"Resource type '{resource_type}' not supported."})

        # Assuming manager has a 'get' async method taking ONLY resource_id
        # REMOVED passing self._api_client
        result = await manager.get(resource_id)
        return result.map_err(self._to_error_details)

    async def update(self, resource_type: str, resource_id: str, config: dict[str, Any]) -> Result[ResourceState, ErrorDetails]:
        # REMOVED self._api_client check
        manager = self._handlers.get(resource_type)
        if manager is None: return Err({"error_code": "UNSUPPORTED_RESOURCE", "message": f"Resource type '{resource_type}' not supported."})

        # Assuming manager has an 'update' async method taking resource_id and config
        # REMOVED passing self._api_client
        result = await manager.update(resource_id, config)
        return result.map_err(self._to_error_details)

    async def delete(self, resource_type: str, resource_id: str) -> Result[None, ErrorDetails]:
        # REMOVED self._api_client check
        manager = self._handlers.get(resource_type)
        if manager is None: return Err({"error_code": "UNSUPPORTED_RESOURCE", "message": f"Resource type '{resource_type}' not supported."})

        # Assuming manager has a 'delete' async method taking ONLY resource_id
        # REMOVED passing self._api_client
        result = await manager.delete(resource_id)
        # map_err works for Result[None, Error] as well
        return result.map_err(self._to_error_details)

    async def list(self, resource_type: str, filters: dict[str, Any] | None = None) -> Result[list[ResourceState], ErrorDetails]:
        # REMOVED self._api_client check
        manager = self._handlers.get(resource_type)
        if manager is None: return Err({"error_code": "UNSUPPORTED_RESOURCE", "message": f"Resource type '{resource_type}' not supported."})

        # Assuming manager has a 'list' async method taking ONLY filters
        # REMOVED passing self._api_client
        result = await manager.list(filters)
        return result.map_err(self._to_error_details)

    # --- Action Interface Implementation ---

    async def execute(self, action_name: str, parameters: dict[str, Any]) -> Result[ActionResult, ErrorDetails]:
        # REMOVED self._api_client check

        executor = self._action_executors.get(action_name)
        if executor is None:
            return Err({"error_code": "UNSUPPORTED_ACTION", "message": f"Action '{action_name}' not supported by {self.provider_name} plugin."}) # Corrected typo

        try:
            # Pass ONLY parameters into the executor function
            # The executor function should return Result[ActionResult, ErrorResponse]
            # REMOVED passing self._api_client
            result = await executor(**parameters)
            # Map potential ErrorResponse to standard ErrorDetails
            return result.map_err(self._to_error_details)
        except TypeError as e:
             # Check if the error is due to unexpected keyword arguments (common if client was expected)
             if "'client'" in str(e):
                 logger.error(f"Executor function for action '{action_name}' might still expect a 'client' argument: {e}", exc_info=True)
                 return Err({"error_code": "INTERNAL_ERROR", "message": f"Action '{action_name}' implementation mismatch (client parameter)."})
             else:
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

    # REMOVED client parameter from proxy methods
    async def _proxy_create(self, **parameters: Any) -> Result[ActionResult, ErrorResponse]:
        resource_type = parameters.get("resource_type")
        config = parameters.get("config")
        if resource_type is None or config is None:
            # Use ErrorDetails structure directly for consistency if ErrorResponse is just a TypedDict
            # return Err(ErrorResponse(status_code=400, error="...")
            return Err({"status_code": 400, "error_code": "INVALID_PARAMETERS", "message": "'resource_type' and 'config' are required for Create action.", "details": None})
        # Call the actual resource creation method
        create_result = await self.create(resource_type, config)
        # Map the result: ResourceState becomes ActionResult
        # Need to handle potential ErrorDetails from self.create
        if create_result.is_err():
             # Assuming self.create returns Result[..., ErrorDetails] now
             err_details = create_result.err_value
             # Convert ErrorDetails back to ErrorResponse for the return type hint? Or change hint?
             # Let's assume the proxy should return Result[ActionResult, ErrorDetails] for consistency
             return Err(err_details) # Pass ErrorDetails through
        else:
             # Map Ok(ResourceState) to Ok(ActionResult)
             return Ok(create_result.ok_value) # Simple mapping for now

    # REMOVED client parameter
    async def _proxy_update(self, **parameters: Any) -> Result[ActionResult, ErrorResponse]:
        resource_type = parameters.get("resource_type")
        resource_id = parameters.get("resource_id")
        config = parameters.get("config")
        if resource_type is None or resource_id is None or config is None:
             return Err({"status_code": 400, "error_code": "INVALID_PARAMETERS", "message":"'resource_type', 'resource_id', and 'config' are required for Update action.", "details": None})
        update_result = await self.update(resource_type, resource_id, config)
        # Handle potential ErrorDetails
        if update_result.is_err():
            return Err(update_result.err_value)
        else:
            return Ok(update_result.ok_value)

    # REMOVED client parameter
    async def _proxy_delete(self, **parameters: Any) -> Result[ActionResult, ErrorResponse]:
        resource_type = parameters.get("resource_type")
        resource_id = parameters.get("resource_id")
        if resource_type is None or resource_id is None:
             return Err({"status_code": 400, "error_code": "INVALID_PARAMETERS", "message":"'resource_type' and 'resource_id' are required for Delete action.", "details": None})
        delete_result = await self.delete(resource_type, resource_id)
        # Handle potential ErrorDetails
        if delete_result.is_err():
            return Err(delete_result.err_value)
        else:
            # If successful (None), return an empty dict for ActionResult
            return Ok({})