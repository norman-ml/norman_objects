from enum import Enum


class DataDomain(str, Enum):
    Audio = "Audio"
    File = "File"
    Float = "Float"
    Image = "Image"
    Integer = "Integer"
    Text = "Text"
    Video = "Video"

    @staticmethod
    def primitive_types():
        return {DataDomain.Float, DataDomain.Image, DataDomain.Text}

    def is_primitive(self):
        return self in DataDomain.primitive_types()
