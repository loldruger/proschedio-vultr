from typing import Literal, TypedDict

class CreateFirewallGroupConfig(TypedDict):
    """
    Data structure used for creating a Vultr Firewall Group.
    """
    description: str

class UpdateFirewallGroupConfig(TypedDict):
    """
    Data structure used for updating a Vultr Firewall Group.
    """
    description: str

class CreateFirewallRuleConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Firewall Rule.
    `ip_type`, `protocol`, `subnet`, and `subnet_size` are required.
    """
    ip_type: Literal["v4", "v6"] # Required
    protocol: Literal["ICMP", "TCP", "UDP", "GRE", "ESP", "AH"] # Required
    subnet: str # Required
    subnet_size: int # Required
    port: str | None # TCP/UDP only. Specific port or colon-separated range.
    source: str | None # If "cloudflare", subnet and subnet_size are ignored.
    notes: str | None