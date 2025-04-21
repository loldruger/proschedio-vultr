import os
from http import HTTPMethod
# Removed Optional import

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse # Updated import
from ..urls import URL_PLAN_METAL # Updated import

class PlansMetal:
    @staticmethod # Add staticmethod decorator
    async def list_metal_plans(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]: # Removed self, updated types and return type
        """
        Get a list of all Bare Metal plans at Vultr.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_PLAN_METAL.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") # Use os.environ

        if per_page is not None:
            request.add_param("per_page", str(per_page)) # Ensure param is string
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()