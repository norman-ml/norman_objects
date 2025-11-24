from enum import Enum


class HttpRequestType(str, Enum):
    """
    Enumeration of supported HTTP request types for model invocation.

    **Values**

    - **Get** — HTTP GET request.
    - **Post** — HTTP POST request.
    - **Put** — HTTP PUT request.
    """
    Get = "Get"
    Post = "Post"
    Put = "Put"
