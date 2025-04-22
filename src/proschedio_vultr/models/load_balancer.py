from typing import Literal, TypedDict


class HealthCheckBody(TypedDict, total=False):
    """
    Data structure representing the health check configuration for a Vultr Load Balancer.
    `protocol` and `port` are required.
    """
    protocol: Literal["HTTPS", "HTTP", "TCP"] # Required
    port: int # Required
    path: str | None # HTTP/HTTPS only
    check_interval: int | None
    response_timeout: int | None
    unhealthy_threshold: int | None
    healthy_threshold: int | None

class ForwardingRuleBody(TypedDict):
    """
    Data structure representing a forwarding rule for a Vultr Load Balancer.
    """
    frontend_protocol: Literal["HTTP", "HTTPS", "TCP"]
    frontend_port: int
    backend_protocol: Literal["HTTP", "HTTPS", "TCP"]
    backend_port: int

class StickySessionBody(TypedDict):
    """
    Data structure representing the sticky session configuration for a Vultr Load Balancer.
    """
    cookie_name: str

class SSLBody(TypedDict, total=False):
    """
    Data structure representing the SSL configuration for a Vultr Load Balancer.
    All fields are optional.
    """
    private_key: str | None
    certificate: str | None
    chain: str | None
    private_key_b64: str | None
    certificate_b64: str | None
    chain_b64: str | None

class FirewallRuleBody(TypedDict):
    """
    Data structure representing a firewall rule for a Vultr Load Balancer.
    """
    port: int
    source: str # "cloudflare" or IP with subnet size
    ip_type: Literal["v4", "v6"]

class AutoSSLBody(TypedDict, total=False):
    """
    Data structure representing the Auto SSL configuration for a Vultr Load Balancer.
    `domain_zone` is required.
    """
    domain_zone: str # Required
    domain_sub: str | None

class CreateLoadBalancerBody(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Load Balancer.
    `region` is required.
    """
    region: str # Required
    balancing_algorithm: Literal["roundrobin", "leastconn"] | None
    ssl_redirect: bool | None
    http2: bool | None
    http3: bool | None
    nodes: int | None # 1-99, odd number, defaults to 1
    proxy_protocol: bool | None
    timeout: int | None # Defaults to 600
    health_check: HealthCheckBody | None
    forwarding_rules: list[ForwardingRuleBody] | None
    sticky_session: StickySessionBody | None
    ssl: SSLBody | None
    label: str | None
    instances: list[str] | None
    firewall_rules: list[FirewallRuleBody] | None
    vpc: str | None
    auto_ssl: AutoSSLBody | None
    global_regions: list[str] | None

class UpdateLoadBalancerBody(TypedDict, total=False):
    """
    Data structure used for updating a Vultr Load Balancer.
    All fields are optional.
    """
    ssl: SSLBody | None
    sticky_session: StickySessionBody | None
    forwarding_rules: list[ForwardingRuleBody] | None
    health_check: HealthCheckBody | None
    proxy_protocol: bool | None
    timeout: int | None
    ssl_redirect: bool | None
    http2: bool | None
    http3: bool | None
    nodes: int | None # 1-99, odd number
    balancing_algorithm: Literal["roundrobin", "leastconn"] | None
    instances: list[str] | None
    label: str | None
    vpc: str | None
    firewall_rules: list[FirewallRuleBody] | None
    auto_ssl: AutoSSLBody | None
    global_regions: list[str] | None
