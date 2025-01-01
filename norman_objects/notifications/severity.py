from enum import Enum


class Severity(str, Enum):
    Error = "error"
    Info = "info"
    Success = "success"
    Warning = "warning"

