import os
from http import HTTPMethod

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import URL_BACKUPS, URL_BACKUPS_ID

class Backups:
    @staticmethod
    async def list_backups(
        instance_id: str | None,
        per_page: int | None,
        cursor: str | None,
    ) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about Backups in your account.

        Args:
            instance_id (str | None): Filter the backups list by Instance id.
            per_page (int | None): Number of items requested per page. Default is 100 and max is 500.
            cursor (str | None): Cursor for paging. See Meta and pagination.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = (Request(URL_BACKUPS.to_str())
            .set_method(HTTPMethod.GET)
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}"))

        if instance_id is not None:
            request.add_param("instance_id", instance_id)
        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def get_backup(backup_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the information for the Backup.

        Args:
            backup_id (str): The Backup id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BACKUPS_ID.assign("backup-id", backup_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )