from enum import Enum


class AssetName(str, Enum):
    File = "File"
    Inference = "Inference"
    Logo = "Logo"
    Requirements = "Requirements"
