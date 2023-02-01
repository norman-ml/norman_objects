from enum import Enum


class ModelParamReceiveFormat(str, Enum):
    File = "File"
    Link = "Link"
    Primitive = "Primitive"
