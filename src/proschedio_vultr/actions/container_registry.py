import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..models.container import CreateContainerRegistryConfig, UpdateContainerRegistryConfig, UpdateContainerRepositoryConfig, UpdateContainerRobotConfig
from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_CONTAINER_LIST, URL_CONTAINER, URL_CONTAINER_ID,
    URL_CONTAINER_REPOSITORY, URL_CONTAINER_REPOSITORY_IMAGE,
    URL_CONTAINER_DOCKER_CREDENTIALS, URL_CONTAINER_KUBERNETES_DOCKER_CREDENTIALS,
    URL_CONTAINER_ROBOTS, URL_CONTAINER_ROBOT, URL_CONTAINER_ARTIFACTS,
    URL_CONTAINER_ARTIFACT, URL_CONTAINER_LIST_REGIONS
)

class ContainerRegistry:
    @staticmethod
    async def list_container_registries(per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        List All Container Registry Subscriptions for this account

        Args:
            per_page (int | None): Number of items requested per page. Default is 100 and max is 500.
            cursor (str | None): Cursor for paging. See Meta and pagination.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_CONTAINER_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if per_page is not None:
            request.add_param("per_page", str(per_page))
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    @staticmethod
    async def create_container_registry(data: CreateContainerRegistryConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Container Registry Subscription

        Args:
            data (CreateContainerRegistryData): The data to create the registry subscription.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_CONTAINER.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def get_container_registry(registry_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a single Container Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_ID.assign("registry-id", registry_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_container_registry(registry_id: str, data: UpdateContainerRegistryConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update a Container Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.
            data (UpdateContainerRegistryData): The data to update the registry subscription.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_CONTAINER_ID.assign("registry-id", registry_id).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def delete_container_registry(registry_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Container Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_ID.assign("registry-id", registry_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_container_repositories(registry_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List All Repositories in a Container Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_REPOSITORY.assign("registry-id", registry_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_container_repository(registry_id: str, repository_image: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a single Repository in a Container Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.
            repository_image (str): Target repository name.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_REPOSITORY_IMAGE.assign("registry-id", registry_id).assign("repository-image", repository_image).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_container_repository(registry_id: str, repository_image: str, data: UpdateContainerRepositoryConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update a Repository in a Container Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.
            repository_image (str): Target repository name.
            data (UpdateContainerRepositoryData): The data to update the repository.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_CONTAINER_REPOSITORY_IMAGE.assign("registry-id", registry_id).assign("repository-image", repository_image).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def delete_container_repository(registry_id: str, repository_image: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Repository from a Container Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.
            repository_image (str): Target repository name.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_REPOSITORY_IMAGE.assign("registry-id", registry_id).assign("repository-image", repository_image).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_docker_credentials(registry_id: str, expiry_seconds: int | None, read_write: bool | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a fresh set of Docker Credentials for this Container Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.
            expiry_seconds (int | None): The duration in seconds for which the credentials are valid (default: 0).
            read_write (bool | None): If false, credentials will be read-only (default: false).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_CONTAINER_DOCKER_CREDENTIALS.assign("registry-id", registry_id).to_str()) \
            .set_method(HTTPMethod.OPTIONS) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if expiry_seconds is not None:
            request.add_param("expiry_seconds", str(expiry_seconds))
        if read_write is not None:
            request.add_param("read_write", str(read_write).lower())

        return await request.request()

    @staticmethod
    async def get_kubernetes_docker_credentials(registry_id: str, expiry_seconds: int | None, read_write: bool | None, base64_encode: bool | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a fresh set of Docker Credentials for this Container Registry Subscription and return them in a Kubernetes friendly YAML format

        Args:
            registry_id (str): The Container Registry Subscription ID.
            expiry_seconds (int | None): The duration in seconds for which the credentials are valid (default: 0).
            read_write (bool | None): If false, credentials will be read-only (default: false).
            base64_encode (bool | None): If true, encodes the output in base64 (default: false).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = Request(URL_CONTAINER_KUBERNETES_DOCKER_CREDENTIALS.assign("registry-id", registry_id).to_str()) \
            .set_method(HTTPMethod.OPTIONS) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")

        if expiry_seconds is not None:
            request.add_param("expiry_seconds", str(expiry_seconds))
        if read_write is not None:
            request.add_param("read_write", str(read_write).lower())
        if base64_encode is not None:
            request.add_param("base64_encode", str(base64_encode).lower())

        return await request.request()

    @staticmethod
    async def list_robots(registry_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List All Robots in a Conainer Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_ROBOTS.assign("registry-id", registry_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_robot(registry_id: str, robot_name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a single Robot in a Container Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.
            robot_name (str): The Robot name.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_ROBOT.assign("registry-id", registry_id).assign("robot-name", robot_name).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_robot(registry_id: str, robot_name: str, data: UpdateContainerRobotConfig) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update the description, disable, duration, and add or remove access, in a Container Registry Subscription Robot

        Args:
            registry_id (str): The Container Registry Subscription ID.
            robot_name (str): The Robot name.
            data (UpdateContainerRobotData): The data to update the robot.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """

        return await Request(URL_CONTAINER_ROBOT.assign("registry-id", registry_id).assign("robot-name", robot_name).to_str()) \
            .set_method(HTTPMethod.PUT) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps(data)) \
            .request()

    @staticmethod
    async def delete_robot(registry_id: str, robot_name: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Deletes a Robot from a Container Registry Subscription

        Args:
            registry_id (str): The Container Registry Subscription ID.
            robot_name (str): The Robot name.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_ROBOT.assign("registry-id", registry_id).assign("robot-name", robot_name).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_artifacts(registry_id: str, repository_image: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        List All Artifacts in a Container Registry Repository

        Args:
            registry_id (str): The Container Registry Subscription ID.
            repository_image (str): The Repository Name.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_ARTIFACTS.assign("registry-id", registry_id).assign("repository-image", repository_image).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_artifact(registry_id: str, repository_image: str, artifact_digest: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get a single Artifact in a Container Registry Repository

        Args:
            registry_id (str): The Container Registry Subscription ID.
            repository_image (str): The Repository Name.
            artifact_digest (str): The Artifact Digest.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_ARTIFACT.assign("registry-id", registry_id).assign("repository-image", repository_image).assign("artifact-digest", artifact_digest).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def delete_artifact(registry_id: str, repository_image: str, artifact_digest: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Deletes an Artifact from a Container Registry Repository

        Args:
            registry_id (str): The Container Registry Subscription ID.
            repository_image (str): The Repository Name.
            artifact_digest (str): The Artifact Digest.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_ARTIFACT.assign("registry-id", registry_id).assign("repository-image", repository_image).assign("artifact-digest", artifact_digest).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def list_regions() -> Result[SuccessResponse, ErrorResponse]:
        """
        List All Regions where a Container Registry can be deployed

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_CONTAINER_LIST_REGIONS.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()