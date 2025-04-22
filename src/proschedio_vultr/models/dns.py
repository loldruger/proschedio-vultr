from typing import Literal, TypedDict

class CreateDomainBody(TypedDict, total=False):
    """
    Data structure used for creating a Vultr DNS Domain.
    `domain` is required.
    """
    domain: str # Required
    ip: str | None
    dns_sec: Literal["enabled", "disabled"] | None

class UpdateDomainBody(TypedDict):
    """
    Data structure used for updating a Vultr DNS Domain.
    """
    dns_sec: Literal["enabled", "disabled"]

class UpdateDomainSOABody(TypedDict, total=False):
    """
    Data structure used for updating the SOA information for a Vultr DNS Domain.
    All fields are optional.
    """
    nsprimary: str | None
    email: str | None

class CreateDomainRecordBody(TypedDict, total=False):
    """
    Data structure used for creating a DNS record.
    `type`, `name`, `data`, and `ttl` are required.
    """
    type: Literal["A", "AAAA", "CNAME", "NS", "MX", "SRV", "TXT", "CAA", "SSHFP"] # Required
    name: str # Required
    data: str # Required
    ttl: int # Required
    priority: int | None # Required for MX and SRV

class UpdateDomainRecordBody(TypedDict, total=False):
    """
    Data structure used for updating a DNS record.
    All fields are optional.
    """
    name: str | None
    data: str | None
    ttl: int | None
    priority: int | None