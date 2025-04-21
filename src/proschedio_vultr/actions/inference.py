import json
import os
from http import HTTPMethod

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_INFERENCE_LIST, URL_INFERENCE_ID, URL_INFERENCE_USAGE
)

class Inference:
    @staticmethod
    async def list_inferences() -> Result[SuccessResponse, ErrorResponse]:
        """
        List all Serverless Inference subscriptions in your account.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_INFERENCE_LIST.to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def create_inference(label: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Create a new Serverless Inference subscription.

        Args:
            label (str): A user-supplied label for this Serverless Inference subscription.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_INFERENCE_LIST.to_str()) \
            .set_method(HTTPMethod.POST) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"label": label})) \
            .request()

    @staticmethod
    async def get_inference(inference_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get information about a Serverless Inference subscription.

        Args:
            inference_id (str): The [Inference ID](#operation/list-inference).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_INFERENCE_ID.assign("inference-id", inference_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def update_inference(inference_id: str, label: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Update information for a Serverless Inference subscription.

        Args:
            inference_id (str): The [Inference ID](#operation/list-inference).
            label (str): A user-supplied label for this Serverless Inference subscription.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_INFERENCE_ID.assign("inference-id", inference_id).to_str()) \
            .set_method(HTTPMethod.PATCH) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .add_header("Content-Type", "application/json") \
            .set_body(json.dumps({"label": label})) \
            .request()

    @staticmethod
    async def delete_inference(inference_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Delete a Serverless Inference subscription.

        Args:
            inference_id (str): The [Inference ID](#operation/list-inference).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_INFERENCE_ID.assign("inference-id", inference_id).to_str()) \
            .set_method(HTTPMethod.DELETE) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()

    @staticmethod
    async def get_inference_usage(inference_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Get usage information for a Serverless Inference subscription.

        Args:
            inference_id (str): The [Inference ID](#operation/list-inference).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_INFERENCE_USAGE.assign("inference-id", inference_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()