import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..models.vpc2 import CreateConfig
from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_VPC2_LIST, URL_VPC2_ID, URL_VPC2_NODES,
    URL_VPC2_ATTACH_NODES, URL_VPC2_DETACH_NODES
)

class VPC2:
    @staticmethod
    async def list_vpc2s(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of all VPC 2.0 networks in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_VPC2_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_vpc2(data: CreateConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new VPC 2.0 network in a `region`.

        Args:
            data (CreateConfig): The data to create the VPC 2.0 network.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        body_dict = {k: v for k, v in data.items() if v is not None}

        return await Request(URL_VPC2_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def get_vpc2(vpc_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a VPC 2.0 network.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VPC2_ID.assign("vpc-id", vpc_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_vpc2(vpc_id: str, description: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for a VPC 2.0 network.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs).
            description (str): The VPC description.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VPC2_ID.assign("vpc-id", vpc_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"description": description})) \
            .request()

    @staticmethod
    async def delete_vpc2(vpc_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a VPC 2.0 network.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_VPC2_ID.assign("vpc-id", vpc_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_vpc2_nodes(vpc_id: str, per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of nodes attached to a VPC 2.0 network.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs).
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_VPC2_NODES.assign("vpc-id", vpc_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def attach_vpc2_nodes(vpc_id: str, data: list[list[str]]) -> Result[SuccessResponse, ErrorResponse]:
        """
        Attach nodes to a VPC 2.0 network.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs).
            data (list[list[str]]): The data to attach nodes to the VPC 2.0 network.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        body_dict = {"nodes": [node for sublist in data for node in sublist]}

        return await Request(URL_VPC2_ATTACH_NODES.assign("vpc-id", vpc_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def detach_vpc2_nodes(vpc_id: str, data: list[list[str]]) -> Result[SuccessResponse, ErrorResponse]:
        """
        Remove nodes from a VPC 2.0 network.

        Args:
            vpc_id (str): The [VPC ID](#operation/list-vpcs).
            data (list[list[str]]): The data to detach nodes from the VPC 2.0 network.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        body_dict = {"nodes": [node for sublist in data for node in sublist]}

        return await Request(URL_VPC2_DETACH_NODES.assign("vpc-id", vpc_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()