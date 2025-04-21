import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import URL_SUBACCOUNT_LIST

# Define placeholder types if models are not yet created
# Using dict for now, replace with Pydantic models if available
CreateSubaccountData = dict

class Subaccounts:
    @staticmethod
    async def list_subaccounts(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about all sub-accounts for your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_SUBACCOUNT_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_subaccount(data: CreateSubaccountData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new subaccount.

        Args:
            data (CreateSubaccountData): The data to create the subaccount.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        # Filter out None values before dumping to JSON
        if hasattr(data, 'to_json'):
            body_dict = {k: v for k, v in data.to_json().items() if v is not None}
        elif isinstance(data, dict):
            body_dict = {k: v for k, v in data.items() if v is not None}
        else:
            raise TypeError("Unsupported type for data")

        return await Request(URL_SUBACCOUNT_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()