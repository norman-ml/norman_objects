from enum import Enum


class ParamReceiveFormat(str, Enum):
    File = "File"
    Link = "Link"
    Primitive = "Primitive"
