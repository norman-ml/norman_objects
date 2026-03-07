from enum import Enum


class SampleEncoding(str, Enum):
    # Audio 
    Flt = "flt"
    FltP = "fltp"
    S16 = "s16"
    S16P = "s16p"
    S32 = "s32"
    S32P = "s32p"

    # Image 
    UInt8 = "uint8"

    # Text 
    U8 = "u8"
    U16Be = "u16be"
    U16Le = "u16le"

    # Video 
    GbrP = "gbrp"
    GbrP10Le = "gbrp10le"
    Gray = "gray"
    Gray10Le = "gray10le"
    Nv12 = "nv12"
    Nv16 = "nv16"
    Nv21 = "nv21"
    Yuv420P = "yuv420p"
    YuvA420P = "yuva420p"
    Yuv420P10Le = "yuv420p10le"
    Yuv422P = "yuv422p"
    Yuv422P10Le = "yuv422p10le"
    Yuv444P = "yuv444p"
    Yuv444P10Le = "yuv444p10le"
    YuvA444P10Le = "yuva444p10le"
    YuvJ420P = "yuvj420p"
    YuvJ422P = "yuvj422p"
    YuvJ444P = "yuvj444p"
