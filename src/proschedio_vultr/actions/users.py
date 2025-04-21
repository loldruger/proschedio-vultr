import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import URL_USER_LIST, URL_USER_ID

CreateUserData = dict
UpdateUserData = dict

class Users:
    @staticmethod
    async def list_users(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of all Users in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_USER_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_user(data: CreateUserData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new User. The `email`, `name`, and `password` attributes are required.

        Args:
            data (CreateUserData): The data to create the User.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        if hasattr(data, 'to_json'):
            body_dict = {k: v for k, v in data.to_json().items() if v is not None}
        elif isinstance(data, dict):
            body_dict = {k: v for k, v in data.items() if v is not None}
        else:
            raise TypeError("Unsupported type for data")

        return await Request(URL_USER_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def get_user(user_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a User.

        Args:
            user_id (str): The [User id](#operation/list-users).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_USER_ID.assign("user-id", user_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_user(user_id: str, data: UpdateUserData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for a User.

        Args:
            user_id (str): The [User id](#operation/list-users).
            data (UpdateUserData): The data to update the User.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        if hasattr(data, 'to_json'):
            body_dict = {k: v for k, v in data.to_json().items() if v is not None}
        elif isinstance(data, dict):
            body_dict = {k: v for k, v in data.items() if v is not None}
        else:
            raise TypeError("Unsupported type for data")

        return await Request(URL_USER_ID.assign("user-id", user_id).to_str()) \
            .set_method(HTTPMethod.PATCH) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def delete_user(user_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a User.

        Args:
            user_id (str): The [User id](#operation/list-users).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_USER_ID.assign("user-id", user_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()