from typing import TypedDict

class NodePoolConfig(TypedDict, total=False):
    """
    Data structure used for creating/updating a Vultr Kubernetes NodePool.
    `node_quantity`, `label`, and `plan` are required for creation.
    `node_quantity` is required for update.
    """
    node_quantity: int # Required for create/update
    label: str # Required for create
    plan: str # Required for create
    tag: str | None
    auto_scaler: bool | None
    min_nodes: int | None
    max_nodes: int | None
    labels: dict[str, str] | None

class CreateKubernetesConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Kubernetes Engine (VKE) cluster.
    `label`, `region`, `version`, and `node_pools` are required.
    """
    label: str # Required
    region: str # Required
    version: str # Required
    node_pools: list[NodePoolConfig] # Required
    ha_controlplanes: bool | None
    enable_firewall: bool | None

class UpdateKubernetesConfig(TypedDict, total=False):
    """
    Data structure used for updating a Vultr Kubernetes Engine (VKE) cluster.
    All fields are optional.
    """
    label: str | None
