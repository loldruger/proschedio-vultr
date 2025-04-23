import os
from http import HTTPMethod
from typing import Literal

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import URL_PLAN

class Plans:
    @staticmethod
    async def list_plans(
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
            "vcg",
        ] | None,
        per_page: int | None,
        cursor: str | None,
        os_: Literal["windows"] | None,
    ) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of all VPS plans at Vultr.

        Args:
            type (Literal["all", "vc2", "vdc", "vhf", "vhp", "voc", "voc-g", "voc-c", "voc-m", "voc-s", "vcg"] | None): Filter the results by type.
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).
            os_ (Literal["windows"] | None): Filter the results by operating system.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_PLAN.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if type is not None:
            request.add_param("type", type)
        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)
        if os_ is not None:
            request.add_param("os", os_)

        return await request.request()