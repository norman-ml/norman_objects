from enum import Enum


class ReceiveFormat(str, Enum):
    """
    Specifies how a signature's data is delivered to or from a model.

    **Values**

    - File — Data is transferred as a file upload or download
    - Link — Data is represented as a URL
    - Primitive — Data is provided as a simple scalar or text
    """
    File = "File"
    Link = "Link"
    Primitive = "Primitive"
