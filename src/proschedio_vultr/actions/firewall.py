import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..models.firewall import CreateFirewallRuleConfig
from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_FIREWALL_GROUP_LIST, URL_FIREWALL_GROUP_ID,
    URL_FIREWALL_GROUP_RULES, URL_FIREWALL_GROUP_RULE
)

class Firewall:
    @staticmethod
    async def list_firewall_groups(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of all Firewall Groups.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_FIREWALL_GROUP_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_firewall_group(description: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Firewall Group.

        Args:
            description (str): The description for the Firewall Group.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_FIREWALL_GROUP_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"description": description})) \
            .request()

    @staticmethod
    async def get_firewall_group(firewall_group_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information for a Firewall Group.

        Args:
            firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_FIREWALL_GROUP_ID.assign("firewall-group-id", firewall_group_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_firewall_group(firewall_group_id: str, description: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for a Firewall Group.

        Args:
            firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).
            description (str): The new description for the Firewall Group.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_FIREWALL_GROUP_ID.assign("firewall-group-id", firewall_group_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"description": description})) \
            .request()

    @staticmethod
    async def delete_firewall_group(firewall_group_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Firewall Group.

        Args:
            firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_FIREWALL_GROUP_ID.assign("firewall-group-id", firewall_group_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_firewall_group_rules(firewall_group_id: str, per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the Firewall Rules for a Firewall Group.

        Args:
            firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_FIREWALL_GROUP_RULES.assign("firewall-group-id", firewall_group_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_firewall_group_rule(firewall_group_id: str, data: CreateFirewallRuleConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a Firewall Rule for a Firewall Group. The attributes `ip_type`, `protocol`, `subnet`, and `subnet_size` are required.

        Args:
            firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).
            data (CreateFirewallRuleConfig): The data to create the Firewall Rule.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_FIREWALL_GROUP_RULES.assign("firewall-group-id", firewall_group_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_firewall_group_rule(firewall_group_id: str, firewall_rule_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a Firewall Rule.

        Args:
            firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).
            firewall_rule_id (str): The [Firewall Rule id](#operation/list-firewall-group-rules).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_FIREWALL_GROUP_RULE.assign("firewall-group-id", firewall_group_id).assign("firewall-rule-id", firewall_rule_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def delete_firewall_group_rule(firewall_group_id: str, firewall_rule_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Firewall Rule.

        Args:
            firewall_group_id (str): The [Firewall Group id](#operation/list-firewall-groups).
            firewall_rule_id (str): The [Firewall Rule id](#operation/list-firewall-group-rules).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_FIREWALL_GROUP_RULE.assign("firewall-group-id", firewall_group_id).assign("firewall-rule-id", firewall_rule_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()