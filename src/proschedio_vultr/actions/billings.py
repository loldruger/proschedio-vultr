import os
from http import HTTPMethod

from rustipy.result import Result

from ..request import Request, SuccessResponse, ErrorResponse
from ..urls import (
    URL_BILLING_LIST_HISTORY, URL_BILLING_INVOICES, URL_BILLING_INVOICE_ID,
    URL_BILLING_INVOICE_ID_ITEMS, URL_BILLING_LIST_PENDING_CHARGES
)


class Billing:
    async def get_billing_history(self, per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Retrieve billing history entries.

        Args:
            per_page (Optional[int]): Number of items requested per page. Default is 100, maximum is 500.
            cursor (Optional[str]): Cursor for pagination.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = (
            Request(URL_BILLING_LIST_HISTORY.to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )

        if per_page is not None:
            request.add_param("per_page", str(per_page)) # Ensure param value is string
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    async def get_billing_invoices(self, per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Retrieve a list of all invoices on the account.

        Args:
            per_page (Optional[int]): Number of items requested per page. Default is 100, maximum is 500.
            cursor (Optional[str]): Cursor for pagination.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = (
            Request(URL_BILLING_INVOICES.to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )

        if per_page is not None:
            request.add_param("per_page", str(per_page)) # Ensure param value is string
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    async def get_billing_invoice_by_id(self, invoice_id: str) -> Result[SuccessResponse, ErrorResponse]:
        """
        Retrieve a specific invoice by ID.

        Args:
            invoice_id (str): The ID of the invoice to retrieve.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BILLING_INVOICE_ID.assign("invoice-id", invoice_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )

    async def get_billing_invoice_items(self, invoice_id: str, per_page: int | None, cursor: str | None) -> Result[SuccessResponse, ErrorResponse]:
        """
        Retrieve line items for a specific invoice.

        Args:
            invoice_id (str): The ID of the invoice.
            per_page (Optional[int]): Number of items requested per page. Default is 100, maximum is 500.
            cursor (Optional[str]): Cursor for pagination.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        request = (
            Request(URL_BILLING_INVOICE_ID_ITEMS.assign("invoice-id", invoice_id).to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
        )

        if per_page is not None:
            request.add_param("per_page", str(per_page)) # Ensure param value is string
        if cursor is not None:
            request.add_param("cursor", cursor)

        return await request.request()

    async def get_pending_charges(self) -> Result[SuccessResponse, ErrorResponse]:
        """
        Retrieve all pending charges for the account.

        Returns:
            Result[SuccessResponse, ErrorResponse]: The result of the API request.
        """
        return (
            await Request(URL_BILLING_LIST_PENDING_CHARGES.to_str())
                .set_method(HTTPMethod.GET)
                .add_header("Authorization", f"Bearer {os.environ.get('VULTR_API_KEY')}")
                .request()
        )