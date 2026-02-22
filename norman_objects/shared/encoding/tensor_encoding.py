from enum import Enum


class TensorEncoding(str, Enum):
    Bool = "bool"
    Float16 = "float16"
    Float32 = "float32"
    Float64 = "float64"
    Int8 = "int8"
    Int16 = "int16"
    Int32 = "int32"
    Int64 = "int64"
    Uint8 = "uint8"
