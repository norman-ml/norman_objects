from enum import Enum


class FunctionState(str, Enum):
    Active = "Active"
    Pending = "Pending"
    Inactive = "Inactive"
    Failed = "Failed"
    Unknown = "Unknown"
