from enum import Enum


class ModelType(str, Enum):
    Api = "Api"
    Pytorch_Export = "Pytorch_Export"
    Pytorch_Script = "Pytorch_Script"
    HuggingFace_Diffuser = "HuggingFace_Diffuser"
    HuggingFace_Transformer = "HuggingFace_Transformer"
    HuggingFace_Generic = "HuggingFace_Generic"
    Other = "Other"
