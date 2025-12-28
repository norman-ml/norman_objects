from enum import Enum


class ReceiveFormat(str, Enum):
    File = "File"
    HuggingFace = "HuggingFace"
    Link = "Link"
    Primitive = "Primitive"
