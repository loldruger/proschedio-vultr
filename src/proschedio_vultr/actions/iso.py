import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import URL_ISO_LIST, URL_ISO_ID, URL_ISO_PUBLIC_LIST

class Iso:
    @staticmethod
    async def list_isos(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the ISOs in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_ISO_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_iso(url: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new ISO in your account from `url`.

        Args:
            url (str): Public URL location of the ISO image to download. Example: https://example.com/my-iso.iso

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_ISO_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"url": url})) \
            .request()

    @staticmethod
    async def get_iso(iso_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information for an ISO.

        Args:
            iso_id (str): The [ISO id](#operation/list-isos).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_ISO_ID.assign("iso-id", iso_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def delete_iso(iso_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete an ISO.

        Args:
            iso_id (str): The [ISO id](#operation/list-isos).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_ISO_ID.assign("iso-id", iso_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_public_isos() -> Result[SuccessResponse, ErrorResponse]:
        """
        List all Vultr Public ISOs.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_ISO_PUBLIC_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()