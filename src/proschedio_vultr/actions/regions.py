import os
from http import HTTPMethod
from typing import Literal

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse # Updated import
from ..urls import URL_REGION, URL_REGION_ID_AVAILABLE # Updated import

class Regions:
    @staticmethod # Add staticmethod decorator
    async def list_regions(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]: # Removed self, updated types and return type
        """
        List all Regions at Vultr.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_REGION.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") # Use os.environ

        if per_page is not None:
            request.add_param("per_page", str(per_page)) # Ensure param is string
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod # Add staticmethod decorator
    async def get_available_plans_in_region(
        region_id: str,
        type: Literal[
            "all",
            "vc2",
            "vdc",
            "vhf",
            "vhp",
            "voc",
            "voc-g",
            "voc-c",
            "voc-m",
            "voc-s",
            "vbm",
            "vcg"
        ] | None,
    ) -> Result[SuccessResponse, ErrorResponse]: # Removed self, updated types and return type
        """
        Get a list of the available plans in Region `region-id`. Not all plans are available in all regions.

        Args:
            region_id (str): The [Region id](#operation/list-regions).
            type (Literal["all", "vc2", "vdc", "vhf", "vhp", "voc", "voc-g", "voc-c", "voc-m", "voc-s", "vbm", "vcg"] | None): Filter the results by type.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_REGION_ID_AVAILABLE.assign("region-id", region_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") # Use os.environ

        if type is not None:
            request.add_param("type", type)

        return await request.request()