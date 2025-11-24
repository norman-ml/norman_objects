from enum import Enum


class InputSource(str, Enum):
    """
    Enumeration describing the origin or delivery mode of an input provided
    to a model invocation.

    **Values**

    - **File** — The input is a physical file (uploaded or stored).
    - **Link** — The input is provided as a URL pointing to external content.
    - **Primitive** — The input is a scalar or text value (e.g., string, number).
    - **Stream** — The input is delivered as a data stream (e.g., audio/video).
    """
    File = "File"
    Link = "Link"
    Primitive = "Primitive"
    Stream = "Stream"
