from typing import Literal, TypedDict

class CreateDatabaseConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Managed Database.
    `database_engine`, `database_engine_version`, `region`, `plan`, and `label` are required.
    """
    database_engine: Literal["mysql", "pg", "valkey", "kafka"] # Required
    database_engine_version: str # Required
    region: str # Required
    plan: str # Required
    label: str # Required
    tag: str | None
    vpc_id: str | None
    maintenance_dow: Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] | None
    maintenance_time: str | None # HH:00 format
    trusted_ips: list[str] | None
    mysql_sql_modes: list[str] | None
    mysql_require_primary_key: bool | None
    mysql_slow_query_log: bool | None
    mysql_long_query_time: int | None
    eviction_policy: str | None # Valkey only

class UpdateDatabaseConfig(TypedDict, total=False):
    """
    Data structure used for updating a Vultr Managed Database.
    All fields are optional.
    """
    region: str | None
    plan: str | None
    label: str | None
    tag: str | None
    vpc_id: str | None
    maintenance_dow: Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] | None
    maintenance_time: str | None # HH:00 format
    cluster_time_zone: str | None # TZ database format
    trusted_ips: list[str] | None
    mysql_sql_modes: list[str] | None
    mysql_require_primary_key: bool | None
    mysql_slow_query_log: bool | None
    mysql_long_query_time: int | None
    eviction_policy: str | None # Valkey only

class CreateDatabaseUserConfig(TypedDict, total=False):
    """
    Data structure used for creating a database user within a Vultr Managed Database.
    `username` is required.
    """
    username: str # Required
    password: str | None # Omit to auto-generate
    encryption: Literal["caching_sha2_password", "mysql_native_password"] | None # MySQL only
    permission: Literal["admin", "read", "write", "readwrite"] | None # Kafka only

class UpdateDatabaseUserConfig(TypedDict, total=False):
    """
    Data structure used for updating a database user within a Vultr Managed Database.
    """
    password: str | None # Can be empty to auto-generate

class UpdateDatabaseUserAccessControlConfig(TypedDict, total=False):
    """
    Data structure used for configuring access control settings for a Managed Database user (Valkey and Kafka engine types only).
    All fields are optional.
    """
    acl_categories: list[str] | None # Valkey
    acl_channels: list[str] | None # Valkey
    acl_commands: list[str] | None # Valkey
    acl_keys: list[str] | None # Valkey
    permission: Literal["admin", "read", "write", "readwrite"] | None # Kafka

class CreateDatabaseLogicalDatabaseConfig(TypedDict):
    """
    Data structure used for creating a new logical database within a Vultr Managed Database (MySQL and PostgreSQL only).
    """
    name: str

class CreateDatabaseTopicConfig(TypedDict):
    """
    Data structure used for creating a new topic within a Vultr Managed Database (Kafka engine types only).
    """
    name: str
    partitions: int
    replication: int
    retention_hours: int
    retention_bytes: int

class UpdateDatabaseTopicConfig(TypedDict):
    """
    Data structure used for updating a topic within a Vultr Managed Database (Kafka engine types only).
    """
    partitions: int
    replication: int
    retention_hours: int
    retention_bytes: int

class CreateDatabaseQuotaConfig(TypedDict):
    """
    Data structure used for creating a new quota within a Vultr Managed Database (Kafka engine types only).
    """
    client_id: int
    consumer_byte_rate: int
    producer_byte_rate: int
    request_percentage: int
    user: str

class StartDatabaseMaintenanceConfig(TypedDict):
    """
    Data structure used for starting a version upgrade for a Vultr Managed Database (PostgreSQL engine types only).
    """
    version: str

class StartDatabaseMigrationConfig(TypedDict, total=False):
    """
    Data structure used for starting a migration to a Vultr Managed Database.
    `host`, `port`, `username`, `password`, and `ssl` are required.
    """
    host: str # Required
    port: int # Required
    username: str # Required (uses `default` for Valkey if empty)
    password: str # Required
    ssl: bool # Required
    database: str | None # Required for MySQL/PostgreSQL, excluded for Valkey
    ignored_databases: str | None # Comma-separated list, excluded for Valkey

class CreateDatabaseReadReplicaConfig(TypedDict):
    """
    Data structure used for creating a read-only replica node for a Vultr Managed Database.
    """
    region: str
    label: str

class RestoreDatabaseFromBackupConfig(TypedDict):
    """
    Data structure used for creating a new Vultr Managed Database from a backup.
    """
    label: str
    type: str
    date: str # YYYY-MM-DD
    time: str # HH-MM-SS (UTC)

class ForkDatabaseFromBackupConfig(TypedDict):
    """
    Data structure used for forking a Vultr Managed Database to a new subscription from a backup.
    """
    label: str
    region: str
    plan: str
    vpc_id: str
    type: str
    date: str # YYYY-MM-DD
    time: str # HH-MM-SS (UTC)

class CreateDatabaseConnectionPoolConfig(TypedDict):
    """
    Data structure used for creating a new connection pool within a Vultr Managed Database (PostgreSQL engine types only).
    """
    name: str
    database: str
    username: str
    mode: str
    size: int

class UpdateDatabaseConnectionPoolConfig(TypedDict):
    """
    Data structure used for updating a connection pool within a Vultr Managed Database (PostgreSQL engine types only).
    """
    database: str
    username: str
    mode: str
    size: int