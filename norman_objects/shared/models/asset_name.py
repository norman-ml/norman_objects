from enum import Enum


class AssetName(str, Enum):
    File = "File"
    Logo = "Logo"
    Inference = "Inference"
    Requirements = "Requirements"
