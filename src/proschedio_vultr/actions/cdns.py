import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..models.cdns import CreatePullZoneConfig, CreatePushZoneConfig, UpdatePullZoneConfig, UpdatePushZoneConfig
from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_CDN_LIST_PULL_ZONES, URL_CDN_PULL_ZONE_ID, URL_CDN_PULL_ZONE_PURGE,
    URL_CDN_PUSH_ZONES, URL_CDN_PUSH_ZONE_ID, URL_CDN_PUSH_ZONE_FILES,
    URL_CDN_PUSH_ZONE_FILE
)

class CDNs:
    @staticmethod
    async def list_cdn_pull_zones() -> Result[SuccessResponse, ErrorResponse]:
        """
        List CDN Pull Zones.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CDN_LIST_PULL_ZONES.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_cdn_pull_zone(data: CreatePullZoneConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new CDN Pull Zone.

        Args:
            data (CreatePullZoneConfig): The data to create the pull zone.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_CDN_LIST_PULL_ZONES.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_cdn_pull_zone(pullzone_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a CDN Pull Zone.

        Args:
            pullzone_id (str): The Pull Zone ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CDN_PULL_ZONE_ID.assign("pullzone-id", pullzone_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_cdn_pull_zone(pullzone_id: str, data: UpdatePullZoneConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for a CDN Pull Zone.

        Args:
            pullzone_id (str): The Pull Zone ID.
            data (UpdatePullZoneData): The data to update the pull zone.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_CDN_PULL_ZONE_ID.assign("pullzone-id", pullzone_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def delete_cdn_pull_zone(pullzone_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a CDN Pull Zone.

        Args:
            pullzone_id (str): The Pull Zone ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CDN_PULL_ZONE_ID.assign("pullzone-id", pullzone_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def purge_cdn_pull_zone_cache(pullzone_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Clears cached content on server proxies so that visitors can get the latest page versions.

        Args:
            pullzone_id (str): The Pull Zone ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CDN_PULL_ZONE_PURGE.assign("pullzone-id", pullzone_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({})) \
            .request()

    @staticmethod
    async def list_cdn_push_zones() -> Result[SuccessResponse, ErrorResponse]:
        """
        List CDN Push Zones.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CDN_PUSH_ZONES.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_cdn_push_zone(data: CreatePushZoneConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new CDN Push Zone.

        Args:
            data (CreatePushZoneData): The data to create the push zone.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_CDN_PUSH_ZONES.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_cdn_push_zone(pushzone_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a CDN Push Zone.

        Args:
            pushzone_id (str): The Push Zone ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CDN_PUSH_ZONE_ID.assign("pushzone-id", pushzone_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_cdn_push_zone(pushzone_id: str, data: UpdatePushZoneConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for a CDN Push Zone.

        Args:
            pushzone_id (str): The Push Zone ID.
            data (UpdatePushZoneConfig): The data to update the push zone.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_CDN_PUSH_ZONE_ID.assign("pushzone-id", pushzone_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def delete_cdn_push_zone(pushzone_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a CDN Push Zone.

        Args:
            pushzone_id (str): The Push Zone ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CDN_PUSH_ZONE_ID.assign("pushzone-id", pushzone_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_cdn_push_zone_files(pushzone_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of files that have been uploaded to a specific CDN Push Zone.

        Args:
            pushzone_id (str): The Push Zone ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CDN_PUSH_ZONE_FILES.assign("pushzone-id", pushzone_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_cdn_push_zone_file(pushzone_id: str, data: CreatePushZoneConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a presigned post endpoint that can be used to upload a file to your Push Zone.

        Args:
            pushzone_id (str): The Push Zone ID.
            data (CreatePushZoneConfig): The data to create the file.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_CDN_PUSH_ZONE_FILES.assign("pushzone-id", pushzone_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_cdn_push_zone_file(pushzone_id: str, file_name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a CDN Push Zone file.

        Args:
            pushzone_id (str): The Push Zone ID.
            file_name (str): The File Name.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CDN_PUSH_ZONE_FILE.assign("pushzone-id", pushzone_id).assign("file-name", file_name).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def delete_cdn_push_zone_file(pushzone_id: str, file_name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a CDN Push Zone file.

        Args:
            pushzone_id (str): The Push Zone ID.
            file_name (str): The File Name.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CDN_PUSH_ZONE_FILE.assign("pushzone-id", pushzone_id).assign("file-name", file_name).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()