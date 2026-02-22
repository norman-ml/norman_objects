from enum import Enum
from functools import cache


class ContainerModality(str, Enum):
    Audio = "Audio"
    File = "File"
    Image = "Image"
    Text = "Text"
    Video = "Video"

    @staticmethod
    @cache
    def primitive_types():
        return {ContainerModality.Text}

    def is_primitive(self):
        return self in ContainerModality.primitive_types()
