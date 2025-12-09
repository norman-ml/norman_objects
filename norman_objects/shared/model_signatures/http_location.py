from enum import Enum


class HttpLocation(str, Enum):
    """
    Specifies where a model signature value should be placed within an HTTP
    request during invocation.

    **Values**

    - **Body** — Value appears in the HTTP request body (e.g., JSON, form-data).
    - **Path** — Value is injected into the URL path (e.g., `/models/{id}`).
    - **Query** — Value is appended as a query parameter (e.g., `?limit=10`).
    """
    Body = "Body"
    Path = "Path"
    Query = "Query"
