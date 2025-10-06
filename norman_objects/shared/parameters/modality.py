from enum import Enum
from functools import cache


class Modality(str, Enum):
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
        return {Modality.Float, Modality.Integer, Modality.Text}

    def is_primitive(self):
        return self in Modality.primitive_types()
