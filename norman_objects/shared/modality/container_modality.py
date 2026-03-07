from enum import Enum
from functools import cache


class ContainerModality(str, Enum):
    Audio = "Audio"
    File = "File"
    Float = "Float"
    Image = "Image"
    Integer = "Integer"
    Text = "Text"
    Video = "Video"

    @staticmethod
    @cache
    def primitive_types():
        return {ContainerModality.Float, ContainerModality.Integer, ContainerModality.Text}

    def is_primitive(self):
        return self in ContainerModality.primitive_types()
