import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import URL_VPC_LIST, URL_VPC_ID

CreateVpcData = dict

class VPCs:
    @staticmethod
    async def list_vpcs(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of all VPCs in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_VPC_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_vpc(data: CreateVpcData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new VPC in a `region`. VPCs should use [RFC1918 private address space](https://tools.ietf.org/html/rfc1918).

        Args:
            data (CreateVpcData): The data to create the VPC.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        if hasattr(data, 'to_json'):
            body_dict = {k: v for k, v in data.to_json().items() if v is not None}
        elif isinstance(data, dict):
            body_dict = {k: v for k, v in data.items() if v is not None}
        else:
            raise TypeError("Unsupported type for data")

        return await Request(URL_VPC_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def get_vpc(vpc_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a VPC.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VPC_ID.assign("vpc-id", vpc_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_vpc(vpc_id: str, description: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for a VPC.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs).
            description (str): The VPC description.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VPC_ID.assign("vpc-id", vpc_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"description": description})) \
            .request()

    @staticmethod
    async def delete_vpc(vpc_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a VPC.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VPC_ID.assign("vpc-id", vpc_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()