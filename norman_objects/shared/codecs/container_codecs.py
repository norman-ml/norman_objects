from enum import Enum


class ContainerCodec(str, Enum):
    # Audio (PyAV formats)
    Adts = "adts"
    Flac = "flac"
    Mp3 = "mp3"
    Ogg = "ogg"
    Wav = "wav"

    # Image (Pillow formats)
    Jpeg = "JPEG"
    Png = "PNG"
    Webp = "WEBP"

    # Video (PyAV formats)
    Matroska = "matroska"
    Mov = "mov"
    Mp4 = "mp4"
    Webm = "webm"
