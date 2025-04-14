import json
import aiohttp
import logging
from http import HTTPMethod
from typing import TypedDict, cast

from rustipy.result import Err, Ok, Result

logger = logging.getLogger(__name__)

class MetaInfo(TypedDict, total=False):
    total: int
    links: dict[str, str | None]

class SuccessResponse(TypedDict):
    status_code: int
    data: dict[str, object] | list[object] | None
    meta: MetaInfo | None

class ErrorResponse(TypedDict):
    status_code: int
    error: str

class Url:
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._uri = ""
    
    def uri(self, token: str) -> 'Url':
        self._uri = token
        return self
    
    def assign(self, placeholder: str, value: str) -> 'Url':
        self._uri = self._uri.replace(f"{{{placeholder}}}", value)
        return self
    
    def to_str(self) -> str:
        return self._base_url + self._uri

class Request:
    def __init__(self, url: str):
        self._url = url
        self._method: HTTPMethod | None = None
        self._headers: dict[str, str] = {}
        self._params: dict[str, str | int] = {}
        self._body: str | None = None

    def set_method(self, method: HTTPMethod) -> 'Request':
        self._method = method
        return self
    
    def add_header(self, key: str, value: str) -> 'Request':
        self._headers[key] = value
        return self
    
    def add_param(self, key: str, value: str | int) -> 'Request':
        self._params[key] = value
        return self
    
    def set_body(self, body: str) -> 'Request':
        self._body = body
        return self
    
    async def request(self) -> Result[SuccessResponse, ErrorResponse]:
        if self._method is None:
            logger.error(f"Request method not set for URL: {self._url}")
            return Err(ErrorResponse(status_code=0, error="Request method not set"))

        async with aiohttp.ClientSession() as session:
            try:
                logger.debug(f"Sending {self._method.name} request to {self._url} with params={self._params}, headers={self._headers}, body={self._body}")
                async with session.request(
                    method=self._method.name,
                    url=self._url,
                    headers=self._headers,
                    params=self._params,
                    json=self._body
                ) as response:
                    status = response.status
                    logger.debug(f"Request to {self._url} returned status {status}")

                    if status == 204:
                        logger.info(f"Request successful (204 No Content): {self._url}")
                        return Ok(SuccessResponse(status_code=status, data=None, meta=None))

                    raw_body: dict[str, object] | list[object] | None = None
                    parsing_error_message: str | None = None
                    try:
                        raw_body = await response.json(content_type=None)
                        logger.debug(f"Raw API response body: {raw_body}")
                    except aiohttp.ContentTypeError:
                        try:
                            text_response = await response.text()
                            error_detail = f"Non-JSON response: {text_response[:100]}..."
                            logger.warning(f"API request to {self._url} returned status {status} with non-JSON body: {text_response}")
                        except Exception as text_err:
                            logger.warning(f"API request to {self._url} returned status {status} with non-JSON body, failed to read text: {text_err}")
                            error_detail = "Non-JSON response, unable to read text."
                        parsing_error_message = f"Status {status}: {error_detail}"
                    except json.JSONDecodeError as json_err:
                        logger.warning(f"API request to {self._url} returned status {status} but failed to decode JSON response: {json_err}")
                        parsing_error_message = f"Status {status}: Failed to decode JSON response"
                    except Exception as e:
                        logger.error(f"Unexpected error processing response body from {self._url} (status {status}): {e}", exc_info=True)
                        parsing_error_message = f"Status {status}: Unexpected error processing response body: {e}"

                    if 200 <= status < 300:
                        if parsing_error_message is not None:
                            logger.warning(f"Request to {self._url} had status {status} but failed body processing: {parsing_error_message}")
                            return Err(ErrorResponse(status_code=status, error=parsing_error_message))

                        data_payload: dict[str, object] | list[object] | None = None
                        meta_payload: MetaInfo | None = None

                        if isinstance(raw_body, dict):
                            possible_data_keys = [k for k in raw_body if k != 'meta']
                            if len(possible_data_keys) == 1:
                                potential_payload = raw_body.get(possible_data_keys[0])
                                # Check if the payload is a dict or list before assigning
                                if isinstance(potential_payload, (dict, list)):
                                    # Cast is safe here because we checked the type
                                    data_payload = cast(dict[str, object] | list[object], potential_payload)
                                elif potential_payload is None:
                                     data_payload = None # Explicitly handle None case
                                else:
                                    logger.warning(f"Expected dict or list for single data key '{possible_data_keys[0]}' in response from {self._url}, but got {type(potential_payload)}. Setting data_payload to None.")
                                    data_payload = None
                            else:
                                # If multiple keys (or zero keys besides meta), treat the dict itself as payload (excluding meta)
                                data_payload = {k: v for k, v in raw_body.items() if k != 'meta'}
                            # Safely get meta information
                            meta_payload = cast(MetaInfo | None, raw_body.get("meta"))
                        # Explicitly check if raw_body is a list
                        elif isinstance(raw_body, list):
                            data_payload = raw_body
                        elif raw_body is None:
                             data_payload = None # Explicitly handle None case
                        else:
                            # Handle cases where raw_body is neither dict, list, nor None (e.g., str, int)
                            logger.warning(f"Expected dict or list as response body from {self._url}, but got {type(raw_body)}. Setting data_payload to None.")
                            data_payload = None

                        logger.info(f"Request successful (Status {status}): {self._url}")
                        return Ok(SuccessResponse(status_code=status, data=data_payload, meta=meta_payload))

                    else:
                        error_message_to_return: str
                        if parsing_error_message is not None:
                            error_message_to_return = parsing_error_message
                        elif isinstance(raw_body, dict) and "error" in raw_body:
                            api_error = str(raw_body.get("error", f"Unknown API error (status {status})"))
                            error_message_to_return = api_error
                        else:
                            error_message_to_return = f"API request failed with status {status}"

                        logger.warning(f"Request failed (Status {status}): {self._url}. Error: {error_message_to_return}. Raw Body: {raw_body}")
                        return Err(ErrorResponse(status_code=status, error=error_message_to_return))

            except aiohttp.ClientError as client_err:
                logger.error(f"Network or client error during request to {self._url}: {client_err}", exc_info=True)
                return Err(ErrorResponse(status_code=0, error=f"Network error: {client_err}"))
            except Exception as general_err:
                logger.error(f"Unexpected error during request execution for {self._url}: {general_err}", exc_info=True)
                return Err(ErrorResponse(status_code=0, error=f"Unexpected error: {general_err}"))

