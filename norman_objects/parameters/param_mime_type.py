from enum import Enum


class ParamMimeType(str, Enum):
    # Mime types will be added as our support extends with time
    Audio_Midi = "Audio_Midi"
    Audio_Mp3 = "Audio_Mp3"
    Audio_Mpeg = "Audio_Mpeg"
    Audio_Wav = "Audio_Wav"
    Audio_Webm = "Audio_Webm"
    Image_Jpeg = "Image_Jpeg"
    Image_Png = "Image_Png"
    Image_Webp = "Image_Webp"
    Text_Plain = "Text_Plain"
    Video_Mp4 = "Video_Mp4"
    Video_Ogg = "Video_Ogg"
    Video_Webm = "Video_Webm"

    @property
    def mime_type(self):
        return self.name.lower().replace("_", "/")
