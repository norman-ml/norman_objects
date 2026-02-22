from enum import Enum


class ChannelCodec(str, Enum):
    # Audio (PyAV codecs)
    Aac = "aac"
    Alac = "alac"
    Flac = "flac"
    LibMp3Lame = "libmp3lame"
    LibOpus = "libopus"
    LibVorbis = "libvorbis"
    PcmF32Le = "pcm_f32le"
    PcmS16Le = "pcm_s16le"
    PcmS24Le = "pcm_s24le"
    PcmS32Le = "pcm_s32le"

    # Image (Pillow modes)
    One = "1"
    Cmyk = "CMYK"
    L = "L"
    P = "P"
    Rgb = "RGB"
    Rgba = "RGBA"
    YCbCr = "YCbCr"

    # Text / Subtitle (PyAV codecs)
    Ass = "ass"
    MovText = "mov_text"
    Subrip = "subrip"
    Webvtt = "webvtt"

    # Video (PyAV codecs)
    Ffv1 = "ffv1"
    LibaomAv1 = "libaom-av1"
    Libvpx = "libvpx"
    LibvpxVp9 = "libvpx-vp9"
    Libx264 = "libx264"
    Libx265 = "libx265"
    Mjpeg = "mjpeg"
    ProresKs = "prores_ks"
