from enum import Enum


class ModelType(str, Enum):
    Api = "Api"
    Pytorch_jit = "Pytorch_jit"
