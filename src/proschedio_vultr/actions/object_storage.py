import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..models.object_storage import CreateConfig
from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_OBJECT_STORAGE_LIST, URL_OBJECT_STORAGE_ID,
    URL_OBJECT_STORAGE_ID_REGENERATE_KEY, URL_OBJECT_STORAGE_CLUSTERS
)

class ObjectStorage:
    @staticmethod
    async def list_object_storages(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of all Object Storage in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_OBJECT_STORAGE_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_object_storage(data: CreateConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create new Object Storage. The `cluster_id` attribute is required.

        Args:
            data (CreateObjectStorageConfig): The data to create the Object Storage.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_OBJECT_STORAGE_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_object_storage(object_storage_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about an Object Storage.

        Args:
            object_storage_id (str): The [Object Storage id](#operation/list-object-storages).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_OBJECT_STORAGE_ID.assign("object-storage-id", object_storage_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_object_storage(object_storage_id: str, label: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update the label for an Object Storage.

        Args:
            object_storage_id (str): The [Object Storage id](#operation/list-object-storages).
            label (str | None): The user-supplied label for the Object Storage.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_OBJECT_STORAGE_ID.assign("object-storage-id", object_storage_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"label": label})) \
            .request()

    @staticmethod
    async def delete_object_storage(object_storage_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete an Object Storage.

        Args:
            object_storage_id (str): The [Object Storage id](#operation/list-object-storages).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_OBJECT_STORAGE_ID.assign("object-storage-id", object_storage_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def regenerate_object_storage_keys(object_storage_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Regenerate the keys for an Object Storage.

        Args:
            object_storage_id (str): The [Object Storage id](#operation/list-object-storages).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_OBJECT_STORAGE_ID_REGENERATE_KEY.assign("object-storage-id", object_storage_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_object_storage_clusters(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of all Object Storage Clusters.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_OBJECT_STORAGE_CLUSTERS.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()