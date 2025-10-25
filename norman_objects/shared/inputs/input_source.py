from enum import Enum


class InputSource(str, Enum):
    File = "File"
    Link = "Link"
    Primitive = "Primitive"
    Storage = "Storage"
    Stream = "Stream"
