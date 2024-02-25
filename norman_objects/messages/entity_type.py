from enum import Enum


class EntityType(str, Enum):
    Model = "Model"
    Asset = "Asset"
    Invocation = "Invocation"
    Input = "Input"
    Output = "Output"
