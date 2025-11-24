from enum import Enum


class OutputFormat(str, Enum):
    """
    Enumeration describing the format in which a model returns its output.

    **Values**

    - **Binary** — Raw binary response (e.g., files, encoded tensors).
    - **Json** — JSON-encoded response body.
    - **Text** — UTF-8 text response.
    """
    Binary = "Binary"
    Json = "Json"
    Text = "Text"
