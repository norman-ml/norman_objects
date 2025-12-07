from enum import Enum
from functools import cache


class DataModality(str, Enum):
    """
    Enumeration of all supported data modalities for model inputs
    and outputs.

    **Values**

    - Audio
    - File
    - Float
    - Image
    - Integer
    - Text
    - Video
    """
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
        return {DataModality.Float, DataModality.Integer, DataModality.Text}

    def is_primitive(self):
        return self in DataModality.primitive_types()
