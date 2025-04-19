import logging
from typing import Any
from collections.abc import Awaitable, Callable
from rustipy.result import Result, Ok, Err
from rustipy.option import Nothing

from ._base_handler import ResourceHandlerInterface
from ..plugin import ResourceState, ActionResult, ErrorDetails
from ..request import ErrorResponse, SuccessResponse
from ..resources import instance as instance_resource_logic
from ..actions.instance import Action as InstanceActions, ActionInstance

logger = logging.getLogger(__name__)

class ServerInstanceHandler(ResourceHandlerInterface):
    """Handles Vultr Server Instance resources and actions."""

    def __init__(self):
        super().__init__()
        # Get the instance action object once
        instance_action_handler: ActionInstance = InstanceActions.instance()

        # Map action names directly to the corresponding methods of ActionInstance
        self._action_executors: dict[str, Callable[..., Awaitable[Result[SuccessResponse, ErrorResponse]]]] = {
            "ReinstallInstance": instance_action_handler.reinstall_instance,
            "GetInstanceBandwidth": instance_action_handler.get_instance_bandwidth,
            "GetInstanceNeighbors": instance_action_handler.get_instance_neighbors,
            "ListInstanceVpcs": instance_action_handler.list_instance_vpcs,
            "GetInstanceIsoStatus": instance_action_handler.get_instance_iso_status,
            "AttachIso": instance_action_handler.attach_instance_iso,
            "DetachIso": instance_action_handler.detach_instance_iso,
            "AttachInstanceVpc": instance_action_handler.attach_instance_vpc,
            "DetachInstanceVpc": instance_action_handler.detach_instance_vpc,
            "GetInstanceBackupSchedule": instance_action_handler.get_instance_backup_schedule,
            "SetInstanceBackupSchedule": instance_action_handler.set_instance_backup_schedule,
            "RestoreInstance": instance_action_handler.restore_instance,
            "ListInstanceIpv4": instance_action_handler.list_instance_ipv4,
            "CreateInstanceIpv4": instance_action_handler.create_instance_ipv4,
            "GetInstanceIpv6": instance_action_handler.get_instance_ipv6,
            "CreateInstanceReverseIpv4": instance_action_handler.create_instance_reverse_ipv4,
            "ListInstanceReverseIpv6": instance_action_handler.list_instance_reverse_ipv6,
            "CreateInstanceReverseIpv6": instance_action_handler.create_instance_reverse_ipv6,
            "SetInstanceReverseIpv4": instance_action_handler.set_instance_reverse_ipv4,
            "DeleteInstanceReverseIpv6": instance_action_handler.delete_instance_reverse_ipv6,
            "HaltInstance": instance_action_handler.halt_instance,
            "GetInstanceUserData": instance_action_handler.get_instance_user_data,
            "GetInstanceUpgrades": instance_action_handler.get_instance_upgrades,
            "RebootInstances": instance_action_handler.reboot_instances,
            "StartInstances": instance_action_handler.start_instances,
            # Add other instance-specific actions mapped directly to their methods
        }

    def _to_error_details(self, error_response: ErrorResponse) -> ErrorDetails:
        # Helper to convert specific error (TypedDict) to generic details
        return {
            "status_code": error_response.get("status_code", 0),
            "error_code": "PROVIDER_ERROR", # Generic code
            "message": error_response.get("error", "Unknown provider error"),
            "details": None # ErrorResponse has no details field
        }

    # --- Resource Lifecycle Methods ---
    # These now call functions in instance_resource_logic directly

    async def create(self, config: dict[str, Any]) -> Result[ResourceState, ErrorDetails]:
        # Assuming instance_resource_logic.create exists and takes config
        # and returns Result[ResourceState, ErrorResponse]
        # TODO: Verify instance_resource_logic.create exists and has correct signature
        try:
            # Assuming create function exists in resources/instance.py
            result = await instance_resource_logic.create(config)
            return result.map_err(self._to_error_details)
        except AttributeError:
             logger.error("Function 'create' not found in resources.instance module.")
             return Err({"error_code": "INTERNAL_ERROR", "message": "Resource creation logic not implemented."})
        except Exception as e:
             logger.error(f"Error during resource creation: {e}", exc_info=True)
             return Err({"error_code": "PROVIDER_ERROR", "message": f"Failed to create resource: {e}"})


    async def get(self, resource_id: str) -> Result[ResourceState, ErrorDetails]:
        # Assuming instance_resource_logic.get exists and takes resource_id
        # TODO: Verify instance_resource_logic.get exists and has correct signature
        try:
            # Assuming get function exists in resources/instance.py
            result = await instance_resource_logic.get(resource_id)
            return result.map_err(self._to_error_details)
        except AttributeError:
            logger.error("Function 'get' not found in resources.instance module.")
            return Err({"error_code": "INTERNAL_ERROR", "message": "Resource get logic not implemented."})
        except Exception as e:
            logger.error(f"Error during resource get: {e}", exc_info=True)
            return Err({"error_code": "PROVIDER_ERROR", "message": f"Failed to get resource {resource_id}: {e}"})

    async def update(self, resource_id: str, config: dict[str, Any]) -> Result[ResourceState, ErrorDetails]:
        # Assuming instance_resource_logic.update exists and takes resource_id, config
        # TODO: Verify instance_resource_logic.update exists and has correct signature
        try:
            # Assuming update function exists in resources/instance.py
            result = await instance_resource_logic.update(resource_id, config)
            return result.map_err(self._to_error_details)
        except AttributeError:
            logger.error("Function 'update' not found in resources.instance module.")
            return Err({"error_code": "INTERNAL_ERROR", "message": "Resource update logic not implemented."})
        except Exception as e:
            logger.error(f"Error during resource update: {e}", exc_info=True)
            return Err({"error_code": "PROVIDER_ERROR", "message": f"Failed to update resource {resource_id}: {e}"})


    async def delete(self, resource_id: str) -> Result[Nothing, ErrorDetails]:
        # Assuming instance_resource_logic.delete exists and takes resource_id
        # It should return Result[None, ErrorResponse] or similar
        # TODO: Verify instance_resource_logic.delete exists and has correct signature
        try:
            # Assuming delete function exists in resources/instance.py
            result = await instance_resource_logic.delete(resource_id)
            # Map error if present, otherwise Ok(None) remains Ok(None)
            return result.map_err(self._to_error_details)
        except AttributeError:
             logger.error("Function 'delete' not found in resources.instance module.")
             return Err({"error_code": "INTERNAL_ERROR", "message": "Resource deletion logic not implemented."})
        except Exception as e:
             logger.error(f"Error during resource deletion: {e}", exc_info=True)
             return Err({"error_code": "PROVIDER_ERROR", "message": f"Failed to delete resource {resource_id}: {e}"})


    async def list(self, filters: dict[str, Any] | None = None) -> Result[list[ResourceState], ErrorDetails]:
        # Assuming instance_resource_logic.list exists and takes filters
        # TODO: Verify instance_resource_logic.list exists and has correct signature
        try:
            # Assuming list function exists in resources/instance.py
            result = await instance_resource_logic.list(filters)
            return result.map_err(self._to_error_details)
        except AttributeError:
             logger.error("Function 'list' not found in resources.instance module.")
             return Err({"error_code": "INTERNAL_ERROR", "message": "Resource listing logic not implemented."})
        except Exception as e:
             logger.error(f"Error during resource listing: {e}", exc_info=True)
             return Err({"error_code": "PROVIDER_ERROR", "message": f"Failed to list resources: {e}"})


    # --- Action Execution Method ---

    async def execute(self, action_name: str, parameters: dict[str, Any]) -> Result[ActionResult, ErrorDetails]:
        """Handles actions specific to this resource type."""
        # Get the executor method directly from the dictionary
        executor_method = self._action_executors.get(action_name)

        if executor_method is None:
            # Handle unsupported actions (same logic as before)
            if action_name in ["CreateServerInstance", "UpdateServerInstance", "DeleteServerInstance"]:
                 logger.error(f"Lifecycle action '{action_name}' should be handled by VultrPlugin proxy methods.")
                 return Err({"error_code": "INTERNAL_ERROR", "message": f"Action '{action_name}' routing error."})
            else:
                 return Err({"error_code": "UNSUPPORTED_ACTION", "message": f"Action '{action_name}' not supported for server instances."})

        try:
            # Call the method obtained directly from the dictionary
            result: Result[SuccessResponse, ErrorResponse] = await executor_method(**parameters)

            # Map the SuccessResponse/ErrorResponse to ActionResult/ErrorDetails (same logic as before)
            if result.is_ok():
                success_data = result.ok_value.get("data", {})
                if success_data is None:
                    return Ok({})
                if isinstance(success_data, dict):
                     return Ok(success_data)
                elif isinstance(success_data, list):
                     return Ok({"items": success_data})
                else:
                     logger.warning(f"Action '{action_name}' returned non-dict/list data: {type(success_data)}. Returning as value.")
                     return Ok({"value": success_data})
            else:
                return Err(self._to_error_details(result.err_value))

        # Removed AttributeError handling here as the method is retrieved directly
        except TypeError as e:
             logger.error(f"Type error executing instance action '{action_name}' with params {parameters}: {e}", exc_info=True)
             return Err({"error_code": "INVALID_PARAMETERS", "message": f"Invalid parameters for action '{action_name}': {e}"})
        except Exception as e:
            logger.error(f"Error executing instance action '{action_name}': {e}", exc_info=True)
            return Err({"error_code": "ACTION_EXECUTION_FAILED", "message": str(e)})

    async def list_actions(self) -> Result[list[str], ErrorDetails]:
        """Lists actions supported by this handler."""
        # Return the keys from the executors dictionary
        return Ok(list(self._action_executors.keys()))
