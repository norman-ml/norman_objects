from enum import Enum


class AssetType(str, Enum):
    File = "File"
    Logo = "Logo"
    Inference = "Inference"
    Requirements = "Requirements"
