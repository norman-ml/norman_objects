from enum import Enum


class Severity(str, Enum):
    Error = "Error"
    Info = "Info"
    Success = "Success"
    Warning = "Warning"
