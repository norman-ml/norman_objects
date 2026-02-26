from enum import Enum


class ChannelEncoding(str, Enum):
    # Audio
    Aac = "aac"
    Alac = "alac"
    Flac = "flac"
    Mp3 = "mp3"
    Mp3Vbr = "mp3_vbr"
    Opus = "opus"
    PcmF32Le = "pcm_f32le"
    PcmS16Le = "pcm_s16le"
    PcmS24Le = "pcm_s24le"
    PcmS32Le = "pcm_s32le"
    Vorbis = "vorbis"

    # Image
    One = "1"
    Cmyk = "cmyk"
    L = "l"
    P = "p"
    Rgb = "rgb"
    Rgba = "rgba"
    YCbCr = "ycbcr"

    # Text (general)
    Utf8 = "utf8"
    Utf16 = "utf16"

    # Text(video container subtitles) 
    Ass = "ass"
    MovText = "mov_text"
    Srt = "srt"
    Vtt = "vtt"

    # Video 
    Av1 = "av1"
    Ffv1 = "ffv1"
    H264 = "h264"
    H265 = "h265"
    Mjpeg = "mjpeg"
    ProresKs = "prores_ks"
    Vp8 = "vp8"
    Vp9 = "vp9"
