from enum import Enum


class ModelHostingLocation(str, Enum):
    External = "External"
    Internal = "Internal"
