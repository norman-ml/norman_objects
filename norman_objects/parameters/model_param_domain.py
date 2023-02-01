from enum import Enum


class ModelParamDomain(str, Enum):
    Audio = "Audio"
    File = "File"
    Float = "Float"
    Image = "Image"
    Integer = "Integer"
    Text = "Text"
    Video = "Video"
