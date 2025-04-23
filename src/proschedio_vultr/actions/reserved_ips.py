import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..models.reserved_ips import CreateReservedIpConfig
from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_RESERVED_IP, URL_RESERVED_IP_ID,
    URL_RESERVED_IP_ATTACH, URL_RESERVED_IP_DETACH, URL_RESERVED_IP_CONVERT
)

class ReservedIPs:
    @staticmethod
    async def list_reserved_ips(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all Reserved IPs in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_RESERVED_IP.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_reserved_ip(data: CreateReservedIpConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Reserved IP. The `region` and `ip_type` attributes are required.

        Args:
            data (CreateReservedIpConfig): The data to create the Reserved IP.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_RESERVED_IP.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_reserved_ip(reserved_ip: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a Reserved IP.

        Args:
            reserved_ip (str): The [Reserved IP id](#operation/list-reserved-ips).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_RESERVED_IP_ID.assign("reserved-ip", reserved_ip).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_reserved_ip(reserved_ip: str, label: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information on a Reserved IP.

        Args:
            reserved_ip (str): The [Reserved IP id](#operation/list-reserved-ips).
            label (str): The user-supplied label.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_RESERVED_IP_ID.assign("reserved-ip", reserved_ip).to_str()) \
            .set_method(HTTPMethod.PATCH) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"label": label})) \
            .request()

    @staticmethod
    async def delete_reserved_ip(reserved_ip: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Reserved IP.

        Args:
            reserved_ip (str): The [Reserved IP id](#operation/list-reserved-ips).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_RESERVED_IP_ID.assign("reserved-ip", reserved_ip).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def attach_reserved_ip(reserved_ip: str, instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Attach a Reserved IP to an compute instance or a baremetal instance - `instance_id`.

        Args:
            reserved_ip (str): The [Reserved IP id](#operation/list-reserved-ips).
            instance_id (str): Attach the Reserved IP to a [Compute Instance id](#operation/list-instances) or a [Bare Metal Instance id](#operation/list-baremetals).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_RESERVED_IP_ATTACH.assign("reserved-ip", reserved_ip).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"instance_id": instance_id})) \
            .request()

    @staticmethod
    async def detach_reserved_ip(reserved_ip: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Detach a Reserved IP.

        Args:
            reserved_ip (str): The [Reserved IP id](#operation/list-reserved-ips).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_RESERVED_IP_DETACH.assign("reserved-ip", reserved_ip).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def convert_to_reserved_ip(ip_address: str, label: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Convert the `ip_address` of an existing [instance](#operation/list-instances) into a Reserved IP.

        Args:
            ip_address (str): The IP address to convert.
            label (str | None): The user-supplied label for the Reserved IP.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_RESERVED_IP_CONVERT.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"ip_address": ip_address, "label": label})) \
            .request()