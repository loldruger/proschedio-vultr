import json
import logging
import os
from http import HTTPMethod
from typing import Literal

from rustipy.result import Result

from ..urls import (
    URL_INSTANCE_BACKUP_SCHEDULE, URL_INSTANCE_BANDWIDTH, URL_INSTANCE_BY_ID,
    URL_INSTANCE_IPV4, URL_INSTANCE_IPV4_REVERSE, URL_INSTANCE_IPV4_REVERSE_DEFAULT,
    URL_INSTANCE_IPV6, URL_INSTANCE_IPV6_REVERSE, URL_INSTANCE_IPV6_REVERSE_IPV6,
    URL_INSTANCE_ISO, URL_INSTANCE_ISO_ATTACH, URL_INSTANCE_ISO_DETACH, URL_INSTANCE_LIST,
    URL_INSTANCE_NEIGHBORS, URL_INSTANCE_REINSTALL, URL_INSTANCE_RESTORE,
    URL_INSTANCE_UPGRADES, URL_INSTANCE_USER_DATA, URL_INSTANCE_VPCS,
    URL_INSTANCE_VPCS_ATTACH, URL_INSTANCE_VPCS_DETACH, URL_INSTANCES_REBOOT,
    URL_INSTANCES_START, URL_INSTANCE_CREATE, URL_INSTANCE_HALT,
)
from ..request import Request, SuccessResponse, ErrorResponse
from ..models.instance import BackupScheduleConfig, CreateConfig, ListConfig, UpdateConfig

logger = logging.getLogger(__name__)

class Instance:
    @staticmethod    
    async def list_(filters: ListConfig | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all VPS instances in your account.
        """
        request = (
            Request(URL_INSTANCE_LIST.to_str()) 
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )

        if filters is not None:
            request.add_param("filters", json.dumps(filters))

        return await request.request()
    @staticmethod
    async def create(config: CreateConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Vultr VPS Instance.
        """
        return (
            await Request(URL_INSTANCE_CREATE.to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps(config))
                .request()
        )
    @staticmethod
    async def get(instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a Vultr Instance.
        """
        return (
            await Request(URL_INSTANCE_BY_ID.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )
    @staticmethod
    async def update(instance_id: str, data: UpdateConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for a Vultr Instance.
        """
        return (
            await Request(URL_INSTANCE_BY_ID.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.PATCH)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps(data))
                .request()
        )
    @staticmethod
    async def delete(instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Vultr Instance.
        """
        return (
            await Request(URL_INSTANCE_BY_ID.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.DELETE)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )
    @staticmethod
    async def reinstall(instance_id: str, hostname: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Reinstall a Vultr Instance using an optional `hostname`. (Vultr specific)
        """
        request = (
            Request(URL_INSTANCE_REINSTALL.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
        )
        
        if hostname is not None:
            request.set_body(json.dumps({"hostname": hostname}))
        
        return await request.request()
    @staticmethod
    async def get_bandwidth(instance_id: str, date_range: int | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get bandwidth information about a Vultr Instance. (Vultr specific)
        """
        request = (
            Request(URL_INSTANCE_BANDWIDTH.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )

        if date_range is not None:
            request.add_param("date_range", date_range)
        
        return await request.request()
    @staticmethod
    async def get_neighbors(instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of other instances in the same location as this Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_NEIGHBORS.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )
    @staticmethod
    async def list_vpcs(instance_id: str, per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        list the VPCs for a Vultr Instance. (Vultr specific)
        """
        request = (
            Request(URL_INSTANCE_VPCS.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )
        if per_page is not None:
            request.add_param("per_page", per_page)
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()
    @staticmethod
    async def get_iso_status(instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the ISO status for a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_ISO.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )
    @staticmethod
    async def attach_iso(instance_id: str, iso_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Attach an ISO to a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_ISO_ATTACH.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"iso_id": iso_id}))
                .request()
        )
    @staticmethod
    async def detach_iso(instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Detach the ISO from a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_ISO_DETACH.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .set_body(json.dumps({}))
                .request()
        )
    @staticmethod
    async def attach_vpc(instance_id: str, vpc_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Attach a VPC to a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_VPCS_ATTACH.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"vpc_id": vpc_id}))
                .request()
        )
    @staticmethod
    async def detach_vpc(instance_id: str, vpc_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Detach a VPC from a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_VPCS_DETACH.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"vpc_id": vpc_id}))
                .request()
        )
    @staticmethod
    async def get_backup_schedule(instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the backup schedule for a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_BACKUP_SCHEDULE.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )
    @staticmethod
    async def set_backup_schedule(instance_id: str, data: BackupScheduleConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Set the backup schedule for a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_BACKUP_SCHEDULE.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps(data))
                .request()
        )
    @staticmethod
    async def restore(instance_id: str, backup_id: str | None, snapshot_id: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Restore a Vultr Instance from a backup or snapshot. (Vultr specific)
        """
        request = (
            Request(URL_INSTANCE_RESTORE.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
        )
        if backup_id is not None:
            request.set_body(json.dumps({"backup_id": backup_id}))
        elif snapshot_id is not None:
            request.set_body(json.dumps({"snapshot_id": snapshot_id}))
        # else: # Consider raising an error if neither is provided
        #     raise ValueError("Either backup_id or snapshot_id must be provided for restore.")

        return await request.request()
    @staticmethod
    async def list_ipv4(instance_id: str, public_network: bool | None, per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        list the IPv4 information for a Vultr Instance. (Vultr specific)
        """
        request = (
            Request(URL_INSTANCE_IPV4.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )

        if public_network is not None:
            request.add_param("public_network", public_network)
        if per_page is not None:
            request.add_param("per_page", per_page)
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()
    @staticmethod
    async def create_ipv4(instance_id: str, reboot: bool | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create an IPv4 address for a Vultr Instance. (Vultr specific)
        """
        request = (
            Request(URL_INSTANCE_IPV4.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
        )
        
        if reboot is not None:
            request.set_body(json.dumps({"reboot": reboot}))

        return await request.request()
    @staticmethod
    async def get_ipv6(instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the IPv6 information for a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_IPV6.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )
    @staticmethod
    async def create_reverse_ipv4(instance_id: str, ip: str, reverse: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a reverse IPv4 entry for a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_IPV4_REVERSE.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"ip": ip, "reverse": reverse}))
                .request()
        )
    @staticmethod
    async def list_reverse_ipv6(instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        list the reverse IPv6 information for a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_IPV6_REVERSE.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )
    @staticmethod
    async def create_reverse_ipv6(instance_id: str, ip: str, reverse: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a reverse IPv6 entry for a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_IPV6_REVERSE.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"ip": ip, "reverse": reverse}))
                .request()
        )
    @staticmethod
    async def set_reverse_ipv4(instance_id: str, ip: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Set a reverse DNS entry for an IPv4 address of a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_IPV4_REVERSE_DEFAULT.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"ip": ip}))
                .request()
        )
    @staticmethod
    async def delete_reverse_ipv6(instance_id: str, ipv6: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete the reverse IPv6 for a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_IPV6_REVERSE_IPV6.assign("instance-id", instance_id).assign("ipv6", ipv6).to_str())
                .set_method(HTTPMethod.DELETE)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )
    @staticmethod
    async def halt(instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Halt a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_HALT.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )
    @staticmethod
    async def get_user_data(instance_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the user data for a Vultr Instance. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCE_USER_DATA.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )
    @staticmethod
    async def get_upgrades(instance_id: str, type: Literal["all", "applications", "os", "plans"] | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get available upgrades for a Vultr Instance. (Vultr specific)
        """
        request = (
            Request(URL_INSTANCE_UPGRADES.assign("instance-id", instance_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )

        if type is not None:
            request.add_param("type", type)

        return await request.request()
    @staticmethod
    async def reboot_many(instance_ids: list[str]) -> Result[SuccessResponse, ErrorResponse]:
        """
        Reboot multiple Vultr Instances. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCES_REBOOT.to_str())
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"instance_ids": instance_ids}))
                .request()
        )
    @staticmethod
    async def start_many(instance_ids: list[str]) -> Result[SuccessResponse, ErrorResponse]:
        """
        Start multiple Vultr Instances. (Vultr specific)
        """
        return (
            await Request(URL_INSTANCES_START.to_str()) # Use the correct URL constant
                .set_method(HTTPMethod.POST)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .add_header("Content-Type", "application/json")
                .set_body(json.dumps({"instance_ids": instance_ids}))
                .request()
        )