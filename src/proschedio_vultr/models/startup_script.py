from typing import Optional, Literal, TypedDict
from http import HTTPMethod

from proschedio import composer
from vultr import get_key
from vultr.apis import Consts

class UpdateStartupScriptBody(TypedDict, total=False):
    """
    Data structure used for updating a Vultr Startup Script.
    All fields are optional.
    """
    name: str | None
    script: str | None # Base64 encoded
    type: Literal["boot", "pxe"] | None

async def get_startup_script(startup_id: str):
    """
    Get information for a Startup Script.

    Args:
        startup_id (str): The [Startup Script id](#operation/list-startup-scripts).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_STARTUP_SCRIPT_ID.assign("startup-id", startup_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()


async def update_startup_script(startup_id: str, data: UpdateStartupScriptBody):
    """
    Update a Startup Script.

    Args:
        startup_id (str): The [Startup Script id](#operation/list-startup-scripts).
        data (UpdateStartupScriptBody): The data to update the Startup Script.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_STARTUP_SCRIPT_ID.assign("startup-id", startup_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data) \
        .request()


async def delete_startup_script(startup_id: str):
    """
    Delete a Startup Script.

    Args:
        startup_id (str): The [Startup Script id](#operation/list-startup-scripts).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(Consts.URL_STARTUP_SCRIPT_ID.assign("startup-id", startup_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()