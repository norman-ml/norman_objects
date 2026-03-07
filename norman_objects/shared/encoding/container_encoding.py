from enum import Enum


class ContainerEncoding(str, Enum):
    # Audio
    Aac = "aac"
    Flac = "flac"
    Mp3 = "mp3"
    Ogg = "ogg"
    Wav = "wav"

    # File (general + model)
    Bin = "bin"
    Pt = "pt"
    Zip = "zip"

    # Image
    Jpg = "jpg"
    Png = "png"
    WebP = "webp"

    # Text
    DocX = "docx"
    Pdf = "pdf"
    Txt = "txt"

    # Video
    Mkv = "mkv"
    Mov = "mov"
    Mp4 = "mp4"
    WebM = "webm"
