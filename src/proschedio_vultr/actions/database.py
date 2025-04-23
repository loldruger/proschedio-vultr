import json
import os
from http import HTTPMethod
from typing import Literal

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..models.database import (
    CreateDatabaseConfig, CreateDatabaseConnectionPoolConfig, CreateDatabaseQuotaConfig,
    CreateDatabaseTopicConfig, CreateDatabaseUserConfig, ForkDatabaseFromBackupConfig,
    RestoreDatabaseFromBackupConfig, StartDatabaseMigrationConfig, UpdateDatabaseConfig,
    UpdateDatabaseConnectionPoolConfig, UpdateDatabaseTopicConfig, UpdateDatabaseUserAccessControlConfig
)
from ..urls import (
    URL_DATABASE_LIST_PLANS, URL_DATABASE_LIST, URL_DATABASE_ID,
    URL_DATABASE_USAGE, URL_DATABASE_USERS, URL_DATABASE_USER,
    URL_DATABASE_USER_ACCESS_CONTROL, URL_DATABASE_LOGICAL_DATABASES,
    URL_DATABASE_LOGICAL_DATABASE, URL_DATABASE_TOPICS, URL_DATABASE_TOPIC,
    URL_DATABASE_QUOTAS, URL_DATABASE_MAINTENANCE, URL_DATABASE_MIGRATION,
    URL_DATABASE_READ_REPLICA, URL_DATABASE_PROMOTE_READ_REPLICA,
    URL_DATABASE_BACKUPS, URL_DATABASE_RESTORE, URL_DATABASE_FORK,
    URL_DATABASE_CONNECTION_POOLS, URL_DATABASE_CONNECTION_POOL,
    URL_DATABASE_ADVANCED_OPTIONS, URL_DATABASE_VERSION_UPGRADE
)

class Database:
    @staticmethod
    async def list_database_plans(engine: Literal["mysql", "pg", "valkey", "kafka"] | None, nodes: int | None, region: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List Managed Database Plans.

        Args:
            engine (Literal["mysql", "pg", "valkey", "kafka"] | None): Filter by engine type.
            nodes (int | None): Filter by number of nodes.
            region (str | None): Filter by [Region id](#operation/list-regions).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_DATABASE_LIST_PLANS.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if engine is not None:
            request.add_param("engine", engine)
        if nodes is not None:
            request.add_param("nodes", str(nodes))
        if region is not None:
            request.add_param("region", region)

        return await request.request()

    @staticmethod
    async def list_databases(label: str | None, tag: str | None, region: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all Managed Databases in your account.

        Args:
            label (str | None): Filter by label.
            tag (str | None): Filter by specific tag.
            region (str | None): Filter by [Region id](#operation/list-regions).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_DATABASE_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if label is not None:
            request.add_param("label", label)
        if tag is not None:
            request.add_param("tag", tag)
        if region is not None:
            request.add_param("region", region)

        return await request.request()

    @staticmethod
    async def create_database(data: CreateDatabaseConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Managed Database in a `region` with the desired `plan`. Supply optional attributes as desired.

        Args:
            data (CreateDatabaseConfig): The data to create the Managed Database.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_database(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_ID.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_database(database_id: str, data: UpdateDatabaseConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for a Managed Database. All attributes are optional. If not set, the attributes will retain their original values.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (UpdateDatabaseConfig): The data to update the Managed Database.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_ID.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def delete_database(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_ID.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_database_usage(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get disk, memory, and vCPU usage information for a Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_USAGE.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_database_users(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all database users within the Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_USERS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_database_user(database_id: str, data: CreateDatabaseUserConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new database user within the Managed Database. Supply optional attributes as desired.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (CreateDatabaseUserConfig): The data to create the database user.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_USERS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_database_user(database_id: str, username: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a Managed Database user.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            username (str): The [database user](#operation/list-database-users).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_USER.assign("database-id", database_id).assign("username", username).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_database_user(database_id: str, username: str, password: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update database user information within a Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            username (str): The [database user](#operation/list-database-users).
            data (UpdateDatabaseUserData): The data to update the database user.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        data = {"password": password} if password is not None else {}
        
        return await Request(URL_DATABASE_USER.assign("database-id", database_id).assign("username", username).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def delete_database_user(database_id: str, username: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a database user within a Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            username (str): The [database user](#operation/list-database-users).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_USER.assign("database-id", database_id).assign("username", username).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_database_user_access_control(database_id: str, username: str, data: UpdateDatabaseUserAccessControlConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Configure access control settings for a Managed Database user (Valkey and Kafka engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            username (str): The [database user](#operation/list-database-users).
            data (UpdateDatabaseUserAccessControlData): The data to update the database user access control.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_USER_ACCESS_CONTROL.assign("database-id", database_id).assign("username", username).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def list_logical_databases(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all logical databases within the Managed Database (MySQL and PostgreSQL only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_LOGICAL_DATABASES.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_logical_database(database_id: str, name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new logical database within the Managed Database (MySQL and PostgreSQL only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (CreateDatabaseLogicalDatabaseData): The data to create the logical database.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        
        data = {"name": name}

        return await Request(URL_DATABASE_LOGICAL_DATABASES.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_logical_database(database_id: str, db_name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a logical database within a Managed Database (MySQL and PostgreSQL only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            db_name (str): The [logical database name](#operation/list-database-dbs).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_LOGICAL_DATABASE.assign("database-id", database_id).assign("db-name", db_name).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def delete_logical_database(database_id: str, db_name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a logical database within a Managed Database (MySQL and PostgreSQL only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            db_name (str): The [logical database name](#operation/list-database-dbs).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_LOGICAL_DATABASE.assign("database-id", database_id).assign("db-name", db_name).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_topics(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all topics within the Managed Database (Kafka engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_TOPICS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_topic(database_id: str, data: CreateDatabaseTopicConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new topic within the Managed Database (Kafka engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (CreateDatabaseTopicData): The data to create the topic.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_TOPICS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_topic(database_id: str, topic_name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a Managed Database topic (Kafka engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            topic_name (str): The [database topic](#operation/list-database-topics).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_TOPIC.assign("database-id", database_id).assign("topic-name", topic_name).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_topic(database_id: str, topic_name: str, data: UpdateDatabaseTopicConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update topic information within a Managed Database (Kafka engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            topic_name (str): The [database topic](#operation/list-database-topics).
            data (UpdateDatabaseTopicData): The data to update the topic.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_TOPIC.assign("database-id", database_id).assign("topic-name", topic_name).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def delete_topic(database_id: str, topic_name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a topic within a Managed Database (Kafka engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            topic_name (str): The [database topic](#operation/list-database-topics).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_TOPIC.assign("database-id", database_id).assign("topic-name", topic_name).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_quotas(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all quotas within the Managed Database (Kafka engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_QUOTAS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_quota(database_id: str, data: CreateDatabaseQuotaConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new quota within the Managed Database (Kafka engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (CreateDatabaseQuotaData): The data to create the quota.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_QUOTAS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def list_maintenance_updates(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all available version upgrades within the Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_DATABASE_MAINTENANCE.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def start_maintenance_update(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Start maintenance updates for the Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_MAINTENANCE.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_migration_status(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        View the status of a migration attached to the Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_MIGRATION.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def start_migration(database_id: str, data: StartDatabaseMigrationConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Start a migration to the Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (StartDatabaseMigrationData): The data to start the migration.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_MIGRATION.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def detach_migration(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Detach a migration from the Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_MIGRATION.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_read_replica(database_id: str, region: str, label: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a read-only replica node for the Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (CreateDatabaseReadReplicaData): The data to create the read replica.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_READ_REPLICA.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"region": region, "label": label})) \
            .request()

    @staticmethod
    async def promote_read_replica(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Promote a read-only replica node to its own primary Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_PROMOTE_READ_REPLICA.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_backup_information(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get backup information for the Managed Database.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_BACKUPS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def restore_from_backup(database_id: str, data: RestoreDatabaseFromBackupConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Managed Database from a backup.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (RestoreDatabaseFromBackupData): The data to restore from backup.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_RESTORE.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def fork_from_backup(database_id: str, data: ForkDatabaseFromBackupConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Fork a Managed Database to a new subscription from a backup.

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (ForkDatabaseFromBackupData): The data to fork from backup.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_FORK.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def list_connection_pools(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all connection pools within the Managed Database (PostgreSQL engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_CONNECTION_POOLS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_connection_pool(database_id: str, data: CreateDatabaseConnectionPoolConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new connection pool within the Managed Database (PostgreSQL engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (CreateDatabaseConnectionPoolData): The data to create the connection pool.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_CONNECTION_POOLS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_connection_pool(database_id: str, pool_name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a Managed Database connection pool (PostgreSQL engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            pool_name (str): The [connection pool name](#operation/list-connection-pools).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        
        return await Request(URL_DATABASE_CONNECTION_POOL.assign("database-id", database_id).assign("pool-name", pool_name).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_connection_pool(database_id: str, pool_name: str, data: UpdateDatabaseConnectionPoolConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update connection-pool information within a Managed Database (PostgreSQL engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            pool_name (str): The [connection pool name](#operation/list-connection-pools).
            data (UpdateDatabaseConnectionPoolData): The data to update the connection pool.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_CONNECTION_POOL.assign("database-id", database_id).assign("pool-name", pool_name).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def delete_connection_pool(database_id: str, pool_name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a connection pool within a Managed Database (PostgreSQL engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            pool_name (str): The [connection pool name](#operation/list-connection-pools).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_CONNECTION_POOL.assign("database-id", database_id).assign("pool-name", pool_name).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_advanced_options(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all configured and available advanced options for the Managed Database (MySQL, PostgreSQL, and Kafka engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_ADVANCED_OPTIONS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_advanced_option(database_id: str, option_name: str, value: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Updates an advanced configuration option for the Managed Database (MySQL, PostgreSQL, and Kafka engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            option_name (str): The name of the advanced option to update.
            value (str): The new value for the advanced option.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_ADVANCED_OPTIONS.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({option_name: value})) \
            .request()

    @staticmethod
    async def list_version_upgrades(database_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List all available version upgrades within the Managed Database (PostgreSQL engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_VERSION_UPGRADE.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def start_version_upgrade(database_id: str, version: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Start a version upgrade for the Managed Database (PostgreSQL engine types only).

        Args:
            database_id (str): The [Managed Database ID](#operation/list-databases).
            data (StartDatabaseMaintenanceData): The data to start the version upgrade.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_DATABASE_VERSION_UPGRADE.assign("database-id", database_id).to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"version": version})) \
            .request()