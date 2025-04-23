import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..models.vfs import CreateConfig
from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_VFS_REGIONS, URL_VFS_LIST, URL_VFS_ID,
    URL_VFS_ATTACHMENTS, URL_VFS_ATTACHMENT
)

class VFS:
    @staticmethod
    async def list_vfs_regions() -> Result[SuccessResponse, ErrorResponse]:
        """
        Retrieve a list of all regions where VFS can be deployed.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VFS_REGIONS.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_vfs_subscriptions(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Retrieve a list of all VFS subscriptions for the account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_VFS_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_vfs_subscription(data: CreateConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new VFS subscription with the specified configuration.

        Args:
            data (CreateVfsConfig): The data to create the VFS subscription.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_VFS_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_vfs_subscription(vfs_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Retrieve a specific VFS subscription by ID.

        Args:
            vfs_id (str): ID of the VFS subscription to retrieve.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VFS_ID.assign("vfs-id", vfs_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_vfs_subscription(vfs_id: str, label: str, storage_size: int) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update a VFS subscription's label or storage size.

        Args:
            vfs_id (str): ID of the VFS subscription to update.
            label (str): The new label for the VFS subscription.
            storage_size (int): The new storage size for the VFS subscription.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_VFS_ID.assign("vfs-id", vfs_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"label": label, "storage_size": storage_size})) \
            .request()

    @staticmethod
    async def delete_vfs_subscription(vfs_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a specific VFS subscription by ID.

        Args:
            vfs_id (str): ID of the VFS subscription to delete.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VFS_ID.assign("vfs-id", vfs_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_vfs_attachments(vfs_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Retrieve a list of all attachments for a specific VFS subscription.

        Args:
            vfs_id (str): ID of the VFS subscription.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VFS_ATTACHMENTS.assign("vfs-id", vfs_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def attach_vps_to_vfs(vfs_id: str, vps_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Attach a VPS instance to a VFS subscription.

        Args:
            vfs_id (str): ID of the VFS subscription.
            vps_id (str): ID of the VPS subscription to attach.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VFS_ATTACHMENT.assign("vfs-id", vfs_id).assign("vps-id", vps_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_vfs_vps_attachment(vfs_id: str, vps_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Retrieve details about a specific VFS-VPS attachment.

        Args:
            vfs_id (str): ID of the VFS subscription.
            vps_id (str): ID of the VPS subscription.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VFS_ATTACHMENT.assign("vfs-id", vfs_id).assign("vps-id", vps_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def detach_vps_from_vfs(vfs_id: str, vps_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Detach a VPS instance from a VFS subscription.

        Args:
            vfs_id (str): ID of the VFS subscription.
            vps_id (str): ID of the VPS subscription to detach.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VFS_ATTACHMENT.assign("vfs-id", vfs_id).assign("vps-id", vps_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()