from enum import Enum


class ModelParamMimeType(str, Enum):
    # Mime types will be added as our support extends with time
    Audio_Midi = "audio/midi"
    Audio_Xmidi = "audio/x-midi"
    Audio_Mp3 = "audio/mp3"
    Audio_Mpeg = "audio/mpeg"
    Audio_Wav = "audio/wav"
    Audio_Xwav = "audio/x-wav"
    Audio_Webm = "audio/webm"
    Image_Jpeg = "image/jpeg"
    Image_Png = "image/png"
    Image_Webp = "image/webp"
    Text_Plain = "text/plain"
