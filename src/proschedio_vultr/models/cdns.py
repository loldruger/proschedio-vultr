from typing import Literal, TypedDict


class CreatePullZoneConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr CDN Pull Zone.
    `label`, `origin_scheme`, and `origin_domain` are required.
    """
    label: str # Required
    origin_scheme: Literal["http", "https"] # Required
    origin_domain: str # Required
    vanity_domain: str | None
    ssl_cert: str | None # Base64 encoded
    ssl_cert_key: str | None # Base64 encoded
    cors: bool | None
    gzip: bool | None
    block_ai: bool | None
    block_bad_bots: bool | None

class UpdatePullZoneConfig(TypedDict, total=False):
    """
    Data structure used for updating a Vultr CDN Pull Zone.
    All fields are optional.
    """
    label: str | None
    vanity_domain: str | None
    ssl_cert: str | None # Base64 encoded
    ssl_cert_key: str | None # Base64 encoded
    cors: bool | None
    gzip: bool | None
    block_ai: bool | None
    block_bad_bots: bool | None
    regions: list[str] | None

class CreatePushZoneConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr CDN Push Zone.
    `label` is required.
    """
    label: str # Required
    vanity_domain: str | None
    ssl_cert: str | None # Base64 encoded
    ssl_cert_key: str | None # Base64 encoded
    cors: bool | None
    gzip: bool | None
    block_ai: bool | None
    block_bad_bots: bool | None

class UpdatePushZoneConfig(TypedDict, total=False):
    """
    Data structure used for updating a Vultr CDN Push Zone.
    All fields are optional.
    """
    label: str | None
    vanity_domain: str | None
    ssl_cert: str | None # Base64 encoded
    ssl_cert_key: str | None # Base64 encoded
    cors: bool | None
    gzip: bool | None
    block_ai: bool | None
    block_bad_bots: bool | None
    regions: list[str] | None

class CreatePushZoneFileConfig(TypedDict):
    """
    Data structure used for creating a presigned post endpoint for uploading a file to a Vultr CDN Push Zone.
    """
    name: str
    size: int