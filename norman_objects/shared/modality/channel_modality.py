from enum import Enum


class ChannelModality(str, Enum):
    Audio = "Audio"
    Image = "Image"
    Text = "Text"
    Video = "Video"
