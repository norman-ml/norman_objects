from enum import Enum


class InputSource(str, Enum):
    File = "File"
    HuggingFace = "HuggingFace"
    Link = "Link"
    Primitive = "Primitive"
    Stream = "Stream"
