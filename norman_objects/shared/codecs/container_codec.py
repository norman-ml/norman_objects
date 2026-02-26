from enum import Enum


class ContainerCodec(str, Enum):
    # Audio (PyAV formats)
    Aac = "aac"  # Added: for decoder mapping
    Adts = "adts"
    Flac = "flac"
    Mp3 = "mp3"
    Ogg = "ogg"
    Wav = "wav"

    # Image (Pillow formats)
    Jpeg = "jpeg"
    Png = "png"
    Webp = "webp"

    # Video (PyAV formats)
    Matroska = "matroska"
    MatroskaWebm = "matroska,webm"
    Mov = "mov"
    MovMp4M4a3gp3g2Mj2 = "mov,mp4,m4a,3gp,3g2,mj2"
    Mp4 = "mp4"
    Webm = "webm"
