import json
import os
from http import HTTPMethod
from typing import Literal

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_DOMAIN_LIST, URL_DOMAIN, URL_DOMAIN_SOA,
    URL_DOMAIN_DNSSEC, URL_DOMAIN_RECORDS, URL_DOMAIN_RECORD
)

CreateDomainData = dict
UpdateDomainData = dict
UpdateDomainSOAData = dict
CreateDomainRecordData = dict
UpdateDomainRecordData = dict


class DNS:
    @staticmethod
    async def list_domains(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all DNS Domains in your account.

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_DOMAIN_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_domain(data: CreateDomainData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a DNS Domain for `domain`. If no `ip` address is supplied a domain with no records will be created.

        Args:
            data (CreateDomainData): The data to create the DNS Domain.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        # Filter out None values before dumping to JSON
        if hasattr(data, 'to_json'):
            body_dict = {k: v for k, v in data.to_json().items() if v is not None}
        elif isinstance(data, dict):
            body_dict = {k: v for k, v in data.items() if v is not None}
        else:
            raise TypeError("Unsupported type for data")

        return await Request(URL_DOMAIN_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def get_domain(dns_domain: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information for the DNS Domain.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DOMAIN.assign("dns-domain", dns_domain).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_domain(dns_domain: str, data: UpdateDomainData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update the DNS Domain.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
            data (UpdateDomainData): The data to update the DNS Domain.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        # Filter out None values before dumping to JSON
        if hasattr(data, 'to_json'):
            body_dict = {k: v for k, v in data.to_json().items() if v is not None}
        elif isinstance(data, dict):
            body_dict = {k: v for k, v in data.items() if v is not None}
        else:
            raise TypeError("Unsupported type for data")

        return await Request(URL_DOMAIN.assign("dns-domain", dns_domain).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def delete_domain(dns_domain: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete the DNS Domain.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DOMAIN.assign("dns-domain", dns_domain).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_domain_soa(dns_domain: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get SOA information for the DNS Domain.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DOMAIN_SOA.assign("dns-domain", dns_domain).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_domain_soa(dns_domain: str, data: UpdateDomainSOAData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update the SOA information for the DNS Domain. All attributes are optional. If not set, the attributes will retain their original values.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
            data (UpdateDomainSOAData): The data to update the SOA information.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        # Filter out None values before dumping to JSON
        if hasattr(data, 'to_json'):
            body_dict = {k: v for k, v in data.to_json().items() if v is not None}
        elif isinstance(data, dict):
            body_dict = {k: v for k, v in data.items() if v is not None}
        else:
            raise TypeError("Unsupported type for data")

        return await Request(URL_DOMAIN_SOA.assign("dns-domain", dns_domain).to_str()) \
            .set_method(HTTPMethod.PATCH) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def get_domain_dnssec(dns_domain: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the DNSSEC information for the DNS Domain.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DOMAIN_DNSSEC.assign("dns-domain", dns_domain).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_domain_records(dns_domain: str, per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the DNS records for the Domain.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
            per_page (int | None): Number of items requested per page. Default is 100 and Max is 500.
            cursor (str | None): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_DOMAIN_RECORDS.assign("dns-domain", dns_domain).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_domain_record(dns_domain: str, data: CreateDomainRecordData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a DNS record.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
            data (CreateDomainRecordData): The data to create the DNS record.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        # Filter out None values before dumping to JSON
        if hasattr(data, 'to_json'):
            body_dict = {k: v for k, v in data.to_json().items() if v is not None}
        elif isinstance(data, dict):
            body_dict = {k: v for k, v in data.items() if v is not None}
        else:
            raise TypeError("Unsupported type for data")

        return await Request(URL_DOMAIN_RECORDS.assign("dns-domain", dns_domain).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def get_domain_record(dns_domain: str, record_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information for a DNS Record.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
            record_id (str): The [DNS Record id](#operation/list-dns-domain-records).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DOMAIN_RECORD.assign("dns-domain", dns_domain).assign("record-id", record_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_domain_record(dns_domain: str, record_id: str, data: UpdateDomainRecordData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update the information for a DNS record. All attributes are optional. If not set, the attributes will retain their original values.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
            record_id (str): The [DNS Record id](#operation/list-dns-domain-records).
            data (UpdateDomainRecordData): The data to update the DNS record.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        # Filter out None values before dumping to JSON
        if hasattr(data, 'to_json'):
            body_dict = {k: v for k, v in data.to_json().items() if v is not None}
        elif isinstance(data, dict):
            body_dict = {k: v for k, v in data.items() if v is not None}
        else:
            raise TypeError("Unsupported type for data")

        return await Request(URL_DOMAIN_RECORD.assign("dns-domain", dns_domain).assign("record-id", record_id).to_str()) \
            .set_method(HTTPMethod.PATCH) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def delete_domain_record(dns_domain: str, record_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete the DNS record.

        Args:
            dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
            record_id (str): The [DNS Record id](#operation/list-dns-domain-records).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DOMAIN_RECORD.assign("dns-domain", dns_domain).assign("record-id", record_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()