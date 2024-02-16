from enum import Enum


class EntityType(str, Enum):
    Image = "Image"
    Asset = "Asset"
    Invocation = "Invocation"
    Input = "Input"
    Output = "Output"
