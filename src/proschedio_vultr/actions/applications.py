import os
from http import HTTPMethod
from typing import Literal

from rustipy.result import Result

from ..request import Request, ErrorResponse, SuccessResponse
from ..urls import URL_APPLICATIONS

class Applications: # Renamed class from BlockStorage to Applications
    @staticmethod
    async def list_applications(
        type: Literal["all", "marketplace", "one-click"] | None, # Use T | None
        per_page: int | None, # Use T | None
        cursor: str | None, # Use T | None
    ) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of all available Applications.

        Args:
            type (Literal["all", "marketplace", "one-click"] | None): Filter the results by type.
            per_page (int | None): Number of applications per page. Default is 100 and max is 500.
            cursor (str | None): Cursor for paging. See Meta and pagination.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request. # Updated return type description
        """

        request = Request(URL_APPLICATIONS.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if type is not None:
            request.add_param("type", type)
        if per_page is not None:
            request.add_param("per_page", str(per_page)) # Ensure param value is string
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()