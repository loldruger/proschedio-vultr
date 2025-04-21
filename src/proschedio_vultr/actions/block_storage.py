import json
import os

from http import HTTPMethod

from rustipy.result import Result

from ..urls import URL_BLOCK_STORAGE, URL_BLOCK_STORAGE_ID, URL_BLOCK_STORAGE_ATTACH, URL_BLOCK_STORAGE_DETACH
from ..request import Request, SuccessResponse, ErrorResponse

class BlockStorage:
    @staticmethod
    async def list_(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all Block Storage in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and max is 500.
            cursor (str | None): Cursor for paging. See Meta and pagination.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = (Request(URL_BLOCK_STORAGE.to_str())
            .set_method(HTTPMethod.GET)
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}"))

        if per_page is not None:
            request.add_param("per_page", per_page)
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create(region: str, size_gb: int, label: str | None, block_type: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create new Block Storage in a `region` with a size of `size_gb`.

        Args:
            region (str): The [Region id](#operation/list-regions) where the Block Storage will be created.
            size_gb (int): Size in GB may range between 10 and 40000, depending on the block_type.
            label (str | None): The user-supplied label.
            block_type (str | None): An optional parameter, that determines the type of block storage volume.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return (
            await Request(URL_BLOCK_STORAGE.to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({k: v for k, v in {"region": region, "size_gb": size_gb, "label": label, "block_type": block_type}.items() if v is not None}))
                .request()
        )

    @staticmethod
    async def get(block_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information for Block Storage.

        Args:
            block_id (str): The Block Storage id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BLOCK_STORAGE_ID.assign("block-id", block_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def update(block_id: str, label: str | None, size_gb: int | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for Block Storage.

        Args:
            block_id (str): The Block Storage id.
            label (str | None): The user-supplied label.
            size_gb (int | None): The new size of the block storage volume in GB. Must be >= current size.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        
        return (
            await Request(URL_BLOCK_STORAGE_ID.assign("block-id", block_id).to_str())
                .set_method(HTTPMethod.PATCH)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({k: v for k, v in {"label": label, "size_gb": size_gb}.items() if v is not None}))
                .request()
        )

    @staticmethod
    async def delete(block_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete Block Storage.

        Args:
            block_id (str): The Block Storage id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BLOCK_STORAGE_ID.assign("block-id", block_id).to_str())
                .set_method(HTTPMethod.DELETE)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def attach(block_id: str, instance_id: str, live: bool | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Attach Block Storage to Instance.

        Args:
            block_id (str): The Block Storage id.
            instance_id (str): The [Instance id](#operation/list-instances) to attach.
            live (bool | None): Attach without restarting the Instance.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return (
            await Request(URL_BLOCK_STORAGE_ATTACH.assign("block-id", block_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({k: v for k, v in {"instance_id": instance_id, "live": live}.items() if v is not None}))
                .request()
        )

    @staticmethod
    async def detach(block_id: str, live: bool | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Detach Block Storage.

        Args:
            block_id (str): The Block Storage id.
            live (bool | None): Detach without restarting the Instance.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return (
            await Request(URL_BLOCK_STORAGE_DETACH.assign("block-id", block_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({k: v for k, v in {"live": live}.items() if v is not None}))
                .request()
        )