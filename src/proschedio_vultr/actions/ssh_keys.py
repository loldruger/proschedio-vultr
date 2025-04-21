import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import URL_SSH_KEY_LIST, URL_SSH_KEY_ID

class SSHKeys:
    @staticmethod
    async def list_ssh_keys(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all SSH Keys in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_SSH_KEY_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_ssh_key(name: str, ssh_key: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new SSH Key for use with future instances.

        Args:
            name (str): The user-supplied name for this SSH Key.
            ssh_key (str): The SSH Key.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_SSH_KEY_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"name": name, "ssh_key": ssh_key})) \
            .request()

    @staticmethod
    async def get_ssh_key(ssh_key_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about an SSH Key.

        Args:
            ssh_key_id (str): The [SSH Key id](#operation/list-ssh-keys).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_SSH_KEY_ID.assign("ssh-key-id", ssh_key_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_ssh_key(ssh_key_id: str, name: str | None, ssh_key: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update an SSH Key.

        Args:
            ssh_key_id (str): The [SSH Key id](#operation/list-ssh-keys).
            name (str | None): The user-supplied name for this SSH Key.
            ssh_key (str | None): The SSH Key.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        body = {}
        if name is not None:
            body["name"] = name
        if ssh_key is not None:
            body["ssh_key"] = ssh_key

        body_dict = {k: v for k, v in body.items() if v is not None}

        return await Request(URL_SSH_KEY_ID.assign("ssh-key-id", ssh_key_id).to_str()) \
            .set_method(HTTPMethod.PATCH) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def delete_ssh_key(ssh_key_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete an SSH Key.

        Args:
            ssh_key_id (str): The [SSH Key id](#operation/list-ssh-keys).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_SSH_KEY_ID.assign("ssh-key-id", ssh_key_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()