import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..models.kubenetes import NodePoolConfig
from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_KUBERNETES_LIST, URL_KUBERNETES_ID, URL_KUBERNETES_DELETE_WITH_LINKED_RESOURCES,
    URL_KUBERNETES_RESOURCES, URL_KUBERNETES_AVAILABLE_UPGRADES, URL_KUBERNETES_UPGRADES,
    URL_KUBERNETES_NODEPOOLS, URL_KUBERNETES_NODEPOOL, URL_KUBERNETES_NODEPOOL_INSTANCE,
    URL_KUBERNETES_NODEPOOL_INSTANCE_RECYCLE, URL_KUBERNETES_CONFIG, URL_KUBERNETES_VERSIONS
)

class Kubernetes:
    @staticmethod
    async def list_kubernetes_clusters() -> Result[SuccessResponse, ErrorResponse]:
        """
        List all Kubernetes clusters currently deployed.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_kubernetes_cluster(label: str, region: str, version: str, node_pools: list[NodePoolConfig], ha_controlplanes: bool | None, enable_firewall: bool | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create Kubernetes Cluster.

        Args:
            label (str): The label for your Kubernetes cluster.
            region (str): Region you want to deploy VKE in.
            version (str): Version of Kubernetes you want to deploy.
            node_pools (list[NodePoolData]): Array of node pool objects.
            ha_controlplanes (bool | None): Whether a highly available control planes configuration should be deployed.
            enable_firewall (bool | None): Whether a [Firewall Group](#tag/firewall) should be deployed and managed by this cluster.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        body = {
            "label": label,
            "region": region,
            "version": version,
            "ha_controlplanes": ha_controlplanes,
            "enable_firewall": enable_firewall,
            "node_pools": node_pools,
        }

        return await Request(URL_KUBERNETES_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body)) \
            .request()

    @staticmethod
    async def get_kubernetes_cluster(vke_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get Kubernetes Cluster.

        Args:
            vke_id (str): The VKE ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_ID.assign("vke-id", vke_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_kubernetes_cluster(vke_id: str, label: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update Kubernetes Cluster.

        Args:
            vke_id (str): The VKE ID.
            label (str | None): Label for the Kubernetes cluster.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        body = {"label": label}
        body_dict = {k: v for k, v in body.items() if v is not None}

        return await Request(URL_KUBERNETES_ID.assign("vke-id", vke_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body_dict)) \
            .request()

    @staticmethod
    async def delete_kubernetes_cluster(vke_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete Kubernetes Cluster.

        Args:
            vke_id (str): The VKE ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_ID.assign("vke-id", vke_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def delete_kubernetes_cluster_and_resources(vke_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete Kubernetes Cluster and all related resources.

        Args:
            vke_id (str): The VKE ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_DELETE_WITH_LINKED_RESOURCES.assign("vke-id", vke_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_kubernetes_resources(vke_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the block storage volumes and load balancers deployed by the specified Kubernetes cluster.

        Args:
            vke_id (str): The VKE ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_RESOURCES.assign("vke-id", vke_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_available_kubernetes_upgrades(vke_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get the available upgrades for the specified Kubernetes cluster.

        Args:
            vke_id (str): The VKE ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_AVAILABLE_UPGRADES.assign("vke-id", vke_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def start_kubernetes_upgrade(vke_id: str, upgrade_version: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Start a Kubernetes cluster upgrade.

        Args:
            vke_id (str): The VKE ID.
            upgrade_version (str): The version you're upgrading to.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_UPGRADES.assign("vke-id", vke_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"upgrade_version": upgrade_version})) \
            .request()

    @staticmethod
    async def list_kubernetes_nodepools(vke_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all available NodePools on a Kubernetes Cluster.

        Args:
            vke_id (str): The VKE ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_NODEPOOLS.assign("vke-id", vke_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_kubernetes_nodepool(vke_id: str, data: NodePoolConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create NodePool for a Existing Kubernetes Cluster.

        Args:
            vke_id (str): The VKE ID.
            data (NodePoolData): The data to create the NodePool.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_KUBERNETES_NODEPOOLS.assign("vke-id", vke_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_kubernetes_nodepool(vke_id: str, nodepool_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get Nodepool from a Kubernetes Cluster.

        Args:
            vke_id (str): The VKE ID.
            nodepool_id (str): The NodePool ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_NODEPOOL.assign("vke-id", vke_id).assign("nodepool-id", nodepool_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_kubernetes_nodepool(vke_id: str, nodepool_id: str, node_quantity: int | None, tag: str | None, auto_scaler: bool | None, min_nodes: int | None, max_nodes: int | None, labels: dict[str, str] | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update a Nodepool on a Kubernetes Cluster.

        Args:
            vke_id (str): The VKE ID.
            nodepool_id (str): The NodePool ID.
            node_quantity (int | None): Number of instances in the NodePool.
            tag (str | None): Tag for node pool.
            auto_scaler (bool | None): Option to use the auto scaler.
            min_nodes (int | None): Auto scaler minimum nodes.
            max_nodes (int | None): Auto scaler maximum nodes.
            labels (dict | None): Map of key/value pairs defining labels.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        body = {
            "node_quantity": node_quantity,
            "tag": tag,
            "auto_scaler": auto_scaler,
            "min_nodes": min_nodes,
            "max_nodes": max_nodes,
            "labels": labels,
        }

        return await Request(URL_KUBERNETES_NODEPOOL.assign("vke-id", vke_id).assign("nodepool-id", nodepool_id).to_str()) \
            .set_method(HTTPMethod.PATCH) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(body)) \
            .request()

    @staticmethod
    async def delete_kubernetes_nodepool(vke_id: str, nodepool_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a NodePool from a Kubernetes Cluster.

        Args:
            vke_id (str): The VKE ID.
            nodepool_id (str): The NodePool ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_NODEPOOL.assign("vke-id", vke_id).assign("nodepool-id", nodepool_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def delete_kubernetes_nodepool_instance(vke_id: str, nodepool_id: str, node_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a single nodepool instance from a given Nodepool.

        Args:
            vke_id (str): The VKE ID.
            nodepool_id (str): The NodePool ID.
            node_id (str): The Instance ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_NODEPOOL_INSTANCE.assign("vke-id", vke_id).assign("nodepool-id", nodepool_id).assign("node-id", node_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def recycle_kubernetes_nodepool_instance(vke_id: str, nodepool_id: str, node_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Recycle a specific NodePool Instance.

        Args:
            vke_id (str): The VKE ID.
            nodepool_id (str): The NodePool ID.
            node_id (str): Node ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_NODEPOOL_INSTANCE_RECYCLE.assign("vke-id", vke_id).assign("nodepool-id", nodepool_id).assign("node-id", node_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_kubernetes_config(vke_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get Kubernetes Cluster Kubeconfig.

        Args:
            vke_id (str): The VKE ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_CONFIG.assign("vke-id", vke_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_kubernetes_versions() -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a list of supported Kubernetes versions.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_KUBERNETES_VERSIONS.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()