import json
import os
from http import HTTPMethod
from typing import Literal, Any # Added Any for flexibility

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import ( # Import specific URLs used in this file
    URL_BARE_METAL, URL_BARE_METAL_ID, URL_BARE_METAL_IPV4, URL_BARE_METAL_IPV6,
    URL_BARE_METAL_IPV4_REVERSE, URL_BARE_METAL_IPV6_REVERSE, URL_BARE_METAL_IPV4_REVERSE_DEFAULT,
    URL_BARE_METAL_IPV6_REVERSE_IPV6, URL_BARE_METAL_START, URL_BARE_METAL_REBOOT,
    URL_BARE_METAL_REINSTALL, URL_BARE_METAL_HALT, URL_BARE_METAL_BANDWIDTH,
    URL_BARE_METALS_HALT, URL_BARE_METALS_REBOOT, URL_BARE_METALS_START, # Corrected URL for reboot_bare_metals
    URL_BARE_METALS_USER_DATA, URL_BARE_METALS_ID_AVAILABLE_UPGRADES, URL_BARE_METALS_ID_VNC,
    URL_BARE_METALS_ATTACH_VPC_TO_INSTANCE, URL_BARE_METALS_DETACH_VPC_FROM_INSTANCE,
    URL_BARE_METALS_VPCS, URL_BARE_METALS_ATTACH_VPC2_TO_INSTANCE,
    URL_BARE_METALS_DETACH_VPC2_FROM_INSTANCE, URL_BARE_METALS_VPCS2
)
# Assuming bare_metal models exist or will be created similar to instance.py models
# from ..models import bare_metal # Import models if they exist

# Define placeholder types if models are not yet created
CreateBareMetalData = dict[str, Any]
UpdateBareMetalData = dict[str, Any]
CreateBareMetalReverseIPv4Data = dict[str, Any]
CreateBareMetalReverseIPv6Data = dict[str, Any]


class BareMetal:
    @staticmethod
    async def list_bare_metals(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all Bare Metal instances in your account.

        Args:
            per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
            cursor (Optional[str]): Cursor for paging. See Meta and pagination.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = (
            Request(URL_BARE_METAL.to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )

        if per_page is not None:
            request.add_param("per_page", str(per_page)) # Ensure param value is string
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_bare_metal(data: CreateBareMetalData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Bare Metal instance in a `region` with the desired `plan`.

        Args:
            data (CreateBareMetalData): The data to create the Bare Metal instance.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        # Filter out None values before dumping to JSON
        body_dict = {k: v for k, v in data.items() if v is not None}
        return (
            await Request(URL_BARE_METAL.to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps(body_dict))
                .request()
        )

    @staticmethod
    async def get_bare_metal(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information for a Bare Metal instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METAL_ID.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def update_bare_metal(baremetal_id: str, data: UpdateBareMetalData) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update a Bare Metal instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            data (UpdateBareMetalData): The data to update the Bare Metal instance.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        # Filter out None values before dumping to JSON
        body_dict = {k: v for k, v in data.items() if v is not None}
        return (
            await Request(URL_BARE_METAL_ID.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.PATCH)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps(body_dict))
                .request()
        )

    @staticmethod
    async def delete_bare_metal(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Bare Metal instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METAL_ID.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.DELETE)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def get_bare_metal_ipv4(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the IPv4 information for the Bare Metal instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METAL_IPV4.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def get_bare_metal_ipv6(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the IPv6 information for the Bare Metal instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METAL_IPV6.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def create_bare_metal_reverse_ipv4(baremetal_id: str, data: CreateBareMetalReverseIPv4Data) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a reverse IPv4 entry for a Bare Metal Instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            data (CreateBareMetalReverseIPv4Data): The data to create the reverse IPv4 entry.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        # Filter out None values before dumping to JSON
        body_dict = {k: v for k, v in data.items() if v is not None}
        return (
            await Request(URL_BARE_METAL_IPV4_REVERSE.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps(body_dict))
                .request()
        )

    @staticmethod
    async def create_bare_metal_reverse_ipv6(baremetal_id: str, data: CreateBareMetalReverseIPv6Data) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a reverse IPv6 entry for a Bare Metal Instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            data (CreateBareMetalReverseIPv6Data): The data to create the reverse IPv6 entry.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        # Filter out None values before dumping to JSON
        body_dict = {k: v for k, v in data.items() if v is not None}
        return (
            await Request(URL_BARE_METAL_IPV6_REVERSE.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps(body_dict))
                .request()
        )

    @staticmethod
    async def set_bare_metal_reverse_ipv4(baremetal_id: str, ip: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Set a reverse DNS entry for an IPv4 address.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            ip (str): The IPv4 address.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METAL_IPV4_REVERSE_DEFAULT.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"ip": ip})) # Use json.dumps
                .request()
        )

    @staticmethod
    async def delete_bare_metal_reverse_ipv6(baremetal_id: str, ipv6: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete the reverse IPv6 for a Bare metal instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            ipv6 (str): The IPv6 address.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METAL_IPV6_REVERSE_IPV6.assign("baremetal-id", baremetal_id).assign("ipv6", ipv6).to_str())
                .set_method(HTTPMethod.DELETE)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def start_bare_metal(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Start the Bare Metal instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METAL_START.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def reboot_bare_metal(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Reboot the Bare Metal instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METAL_REBOOT.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def reinstall_bare_metal(baremetal_id: str, hostname: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Reinstall the Bare Metal instance using an optional `hostname`.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            hostname (Optional[str]): The hostname to use when reinstalling this bare metal server.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = (
            Request(URL_BARE_METAL_REINSTALL.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
        )

        body_dict = {}
        if hostname is not None:
            body_dict["hostname"] = hostname
        request.set_body(json.dumps(body_dict)) # Send empty JSON {} if hostname is None

        return await request.request()

    @staticmethod
    async def halt_bare_metal(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Halt the Bare Metal instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METAL_HALT.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def get_bare_metal_bandwidth(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get bandwidth information for the Bare Metal instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METAL_BANDWIDTH.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def halt_bare_metals(baremetal_ids: list[str]) -> Result[SuccessResponse, ErrorResponse]:
        """
        Halt Bare Metals.

        Args:
            baremetal_ids (list[str]): Array of Bare Metal instance ids to halt.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METALS_HALT.to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"baremetal_ids": baremetal_ids}))
                .request()
        )

    @staticmethod
    async def reboot_bare_metals(baremetal_ids: list[str]) -> Result[SuccessResponse, ErrorResponse]:
        """
        Reboot Bare Metals.

        Args:
            baremetal_ids (list[str]): Array of Bare Metal instance ids to reboot.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METALS_REBOOT.to_str()) # Corrected URL
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"baremetal_ids": baremetal_ids}))
                .request()
        )

    @staticmethod
    async def start_bare_metals(baremetal_ids: list[str]) -> Result[SuccessResponse, ErrorResponse]:
        """
        Start Bare Metals.

        Args:
            baremetal_ids (list[str]): Array of Bare Metal instance ids to start.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METALS_START.to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"baremetal_ids": baremetal_ids}))
                .request()
        )

    @staticmethod
    async def get_bare_metal_user_data(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the user-supplied, base64 encoded [user data] for a Bare Metal.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METALS_USER_DATA.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def get_bare_metal_available_upgrades(baremetal_id: str, type: Literal["all", "applications", "os", "plans"] | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get available upgrades for a Bare Metal.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            type (Optional[Literal["all", "applications", "os", "plans"]]): Filter upgrade by type.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = (
            Request(URL_BARE_METALS_ID_AVAILABLE_UPGRADES.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )

        if type is not None:
            request.add_param("type", type)

        return await request.request()

    @staticmethod
    async def get_bare_metal_vnc_url(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the VNC URL for a Bare Metal.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METALS_ID_VNC.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def attach_vpc_to_bare_metal(baremetal_id: str, vpc_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Attach a VPC Network to a Bare Metal Instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            vpc_id (str): The [VPC ID](#operation/list-vpcs) to attach.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METALS_ATTACH_VPC_TO_INSTANCE.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"vpc_id": vpc_id})) # Use json.dumps
                .request()
        )

    @staticmethod
    async def detach_vpc_from_bare_metal(baremetal_id: str, vpc_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Detach a VPC Network from a Bare Metal Instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            vpc_id (str): The [VPC ID](#operation/list-vpcs) to detach.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METALS_DETACH_VPC_FROM_INSTANCE.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"vpc_id": vpc_id})) # Use json.dumps
                .request()
        )

    @staticmethod
    async def list_bare_metal_vpcs(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List the VPC networks for a Bare Metal Instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METALS_VPCS.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def attach_vpc2_to_bare_metal(baremetal_id: str, vpc_id: str | None, ip_address: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Attach a VPC 2.0 Network to a Bare Metal Instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            vpc_id (str | None): The [VPC ID](#operation/list-vpc2) to attach.
            ip_address (str | None): The IP address to use for this instance on the attached VPC 2.0 network.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        body = {}

        if vpc_id is not None:
            body["vpc_id"] = vpc_id

        if ip_address is not None:
            body["ip_address"] = ip_address

        return (
            await Request(URL_BARE_METALS_ATTACH_VPC2_TO_INSTANCE.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps(body)) # Use json.dumps
                .request()
        )

    @staticmethod
    async def detach_vpc2_from_bare_metal(baremetal_id: str, vpc_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Detach a VPC 2.0 Network from a Bare Metal Instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.
            vpc_id (str): The [VPC ID](#operation/list-vpc2) to detach.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METALS_DETACH_VPC2_FROM_INSTANCE.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"vpc_id": vpc_id})) # Use json.dumps
                .request()
        )

    @staticmethod
    async def list_bare_metal_vpc2s(baremetal_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List the VPC 2.0 networks for a Bare Metal Instance.

        Args:
            baremetal_id (str): The Bare Metal instance id.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BARE_METALS_VPCS2.assign("baremetal-id", baremetal_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )