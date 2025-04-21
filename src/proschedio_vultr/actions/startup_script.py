import json
import os
from http import HTTPMethod
from typing import Literal

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import URL_STARTUP_SCRIPT_LIST, URL_STARTUP_SCRIPT_ID

UpdateStartupScriptData = dict

class StartupScript:
    @staticmethod
    async def list_startup_scripts(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of all Startup Scripts in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_STARTUP_SCRIPT_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_startup_script(name: str, script: str, type: Literal["boot", "pxe"] | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Startup Script in your account.

        Args:
            name (str): The name of the Startup Script.
            script (str): The Startup Script contents.
            type (Literal["boot", "pxe"] | None): The Startup Script type. Default: "boot"

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        body = {
            "name": name,
            "script": script,
            "type": type,
        }
        body_dict = {k: v for k, v in body.items() if v is not None}

        return await Request(URL_STARTUP_SCRIPT_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def get_startup_script(startup_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information for a Startup Script.

        Args:
            startup_id (str): The [Startup Script id](#operation/list-startup-scripts).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_STARTUP_SCRIPT_ID.assign("startup-id", startup_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_startup_script(startup_id: str, data: UpdateStartupScriptData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update a Startup Script.

        Args:
            startup_id (str): The [Startup Script id](#operation/list-startup-scripts).
            data (UpdateStartupScriptData): The data to update the Startup Script.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        if hasattr(data, 'to_json'):
            body_dict = {k: v for k, v in data.to_json().items() if v is not None}
        elif isinstance(data, dict):
            body_dict = {k: v for k, v in data.items() if v is not None}
        else:
            raise TypeError("Unsupported type for data")

        return await Request(URL_STARTUP_SCRIPT_ID.assign("startup-id", startup_id).to_str()) \
            .set_method(HTTPMethod.PATCH) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def delete_startup_script(startup_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Startup Script.

        Args:
            startup_id (str): The [Startup Script id](#operation/list-startup-scripts).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_STARTUP_SCRIPT_ID.assign("startup-id", startup_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()