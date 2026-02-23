from enum import Enum


class ChannelModality(str, Enum):
    Audio = "Audio"
    Float = "Float"
    Image = "Image"
    Integer = "Integer"
    Text = "Text"
    Video = "Video"
