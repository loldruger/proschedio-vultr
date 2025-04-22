from typing import TypedDict

class CreateConfig(TypedDict, total=False):
    """
    Data structure used for creating a Vultr Subaccount.

    email (str): Create a new sub-account with this email address.
    subaccount_name (str): Your name for this sub-account.
    subaccount_id (str): Your ID for this sub-account.
    """
    email: str
    subaccount_name: str
    subaccount_id: str
