from enum import Enum


class ReceiveFormat(str, Enum):
    File = "File"
    Link = "Link"
    Primitive = "Primitive"
