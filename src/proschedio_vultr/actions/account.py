import os

from http import HTTPMethod

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import URL_ACCOUNT, URL_ACCOUNT_BANDWIDTH

class Account:
    @staticmethod
    async def get_account_info() -> Result[SuccessResponse, ErrorResponse]:
        """
        Get your Vultr account, permission, and billing information.

        Returns:
            requests.Response: The response from the API.
        """

        return (
            await Request(URL_ACCOUNT.to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    @staticmethod
    async def get_account_bandwidth() -> Result[SuccessResponse, ErrorResponse]:
        """
        Get your Vultr account bandwidth information.

        Returns:
            requests.Response: The response from the API.
        """
        
        return (
            await Request(URL_ACCOUNT_BANDWIDTH.to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )