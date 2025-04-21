import os
from http import HTTPMethod

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse # Updated import
from ..urls import URL_MARKETPLACE_APP_VARIABLES # Updated import

class Marketplace:
    @staticmethod # Add staticmethod decorator
    async def get_marketplace_app_variables(image_id: str) -> Result[SuccessResponse, ErrorResponse]: # Removed self, updated return type
        """
        List all user-supplied variables for a Marketplace App.

        Args:
            image_id (str): The application's [Image ID](#operation/list-applications).

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return await Request(URL_MARKETPLACE_APP_VARIABLES.assign("image-id", image_id).to_str()) \
            .set_method(HTTPMethod.GET) \
            .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}") \
            .request()