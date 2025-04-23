import json
import os
from http import HTTPMethod

from proschedio_vultr.models.load_balancer import CreateLoadBalancerConfig, ForwardingRuleConfig, UpdateLoadBalancerConfig
from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_LOAD_BALANCER_LIST, URL_LOAD_BALANCER_CREATE, URL_LOAD_BALANCER_ID,
    URL_LOAD_BALANCER_SSL, URL_LOAD_BALANCER_AUTO_SSL,
    URL_LOAD_BALANCER_FORWARDING_RULES, URL_LOAD_BALANCER_FORWARDING_RULE,
    URL_LOAD_BALANCER_FIREWALL_RULES, URL_LOAD_BALANCER_FIREWALL_RULE
)

class LoadBalancers:
    @staticmethod
    async def list_load_balancers(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List the Load Balancers in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_LOAD_BALANCER_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_load_balancer(data: CreateLoadBalancerConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Load Balancer in a particular `region`.

        Args:
            data (CreateLoadBalancerConfig): The data to create the Load Balancer.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_LOAD_BALANCER_CREATE.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_load_balancer(load_balancer_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information for a Load Balancer.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_LOAD_BALANCER_ID.assign("load-balancer-id", load_balancer_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_load_balancer(load_balancer_id: str, data: UpdateLoadBalancerConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for a Load Balancer. All attributes are optional. If not set, the attributes will retain their original values.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
            data (UpdateLoadBalancerConfig): The data to update the Load Balancer.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_LOAD_BALANCER_ID.assign("load-balancer-id", load_balancer_id).to_str()) \
            .set_method(HTTPMethod.PATCH) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def delete_load_balancer(load_balancer_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Load Balancer.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_LOAD_BALANCER_ID.assign("load-balancer-id", load_balancer_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def delete_load_balancer_ssl(load_balancer_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Load Balancer SSL.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_LOAD_BALANCER_SSL.assign("load-balancer-id", load_balancer_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def delete_load_balancer_auto_ssl(load_balancer_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Remove a Load Balancer Auto SSL. This will not remove an ssl certificate from the load balancer.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_LOAD_BALANCER_AUTO_SSL.assign("load-balancer-id", load_balancer_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_load_balancer_forwarding_rules(load_balancer_id: str, per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List the fowarding rules for a Load Balancer.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        request = Request(URL_LOAD_BALANCER_FORWARDING_RULES.assign("load-balancer-id", load_balancer_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_load_balancer_forwarding_rule(load_balancer_id: str, data: ForwardingRuleConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new forwarding rule for a Load Balancer.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
            data (ForwardingRuleConfig): The data to create the forwarding rule.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_LOAD_BALANCER_FORWARDING_RULES.assign("load-balancer-id", load_balancer_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_load_balancer_forwarding_rule(load_balancer_id: str, forwarding_rule_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information for a Forwarding Rule on a Load Balancer.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
            forwarding_rule_id (str): The [Forwarding Rule id](#operation/list-load-balancer-forwarding-rules).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_LOAD_BALANCER_FORWARDING_RULE.assign("load-balancer-id", load_balancer_id).assign("forwarding-rule-id", forwarding_rule_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def delete_load_balancer_forwarding_rule(load_balancer_id: str, forwarding_rule_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Forwarding Rule on a Load Balancer.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
            forwarding_rule_id (str): The [Forwarding Rule id](#operation/list-load-balancer-forwarding-rules).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_LOAD_BALANCER_FORWARDING_RULE.assign("load-balancer-id", load_balancer_id).assign("forwarding-rule-id", forwarding_rule_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_load_balancer_firewall_rules(load_balancer_id: str, per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List the firewall rules for a Load Balancer.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        request = Request(URL_LOAD_BALANCER_FIREWALL_RULES.assign("load-balancer-id", load_balancer_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def get_load_balancer_firewall_rule(load_balancer_id: str, firewall_rule_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a firewall rule for a Load Balancer.

        Args:
            load_balancer_id (str): The [Load Balancer id](#operation/list-load-balancers).
            firewall_rule_id (str): The [Firewall Rule id](#operation/list-loadbalancer-firewall-rules).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_LOAD_BALANCER_FIREWALL_RULE.assign("load-balancer-id", load_balancer_id).assign("firewall-rule-id", firewall_rule_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()