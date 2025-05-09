import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..models.snapshots import CreateSnapshotFromUrlConfig
from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_SNAPSHOT_LIST, URL_SNAPSHOT_ID, URL_SNAPSHOT_CREATE_FROM_URL
)

class Snapshots:
    @staticmethod
    async def list_snapshots(
        description: str | None,
        per_page: int | None,
        cursor: str | None,
    ) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about all Snapshots in your account.

        Args:
            description (str | None): Filter the list of Snapshots by `description`.
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_SNAPSHOT_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if description is not None:
            request.add_param("description", description)
        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_snapshot(instance_id: str, description: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Snapshot for `instance_id`.

        Args:
            instance_id (str): The ID of the instance to create the Snapshot for.
            description (str | None): The optional description for the Snapshot.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_SNAPSHOT_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"instance_id": instance_id, "description": description})) \
            .request()

    @staticmethod
    async def get_snapshot(snapshot_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a Snapshot.

        Args:
            snapshot_id (str): The [Snapshot id](#operation/list-snapshots).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_SNAPSHOT_ID.assign("snapshot-id", snapshot_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_snapshot(snapshot_id: str, description: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update the description for a Snapshot.

        Args:
            snapshot_id (str): The [Snapshot id](#operation/list-snapshots).
            description (str): The user-supplied description for the Snapshot.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_SNAPSHOT_ID.assign("snapshot-id", snapshot_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"description": description})) \
            .request()

    @staticmethod
    async def delete_snapshot(snapshot_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Snapshot.

        Args:
            snapshot_id (str): The [Snapshot id](#operation/list-snapshots).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_SNAPSHOT_ID.assign("snapshot-id", snapshot_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_snapshot_from_url(data: CreateSnapshotFromUrlConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Snapshot from a RAW image located at `url`.

        Args:
            data (CreateSnapshotFromUrlConfig): The data to create the Snapshot from URL.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_SNAPSHOT_CREATE_FROM_URL.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()