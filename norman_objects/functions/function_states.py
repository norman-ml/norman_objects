from enum import Enum


class FunctionStates(str, Enum):
    Active = "Active"
    Pending = "Pending"
    Inactive = "Inactive"
    Failed = "Failed"
    Unknown = "Unknown"
