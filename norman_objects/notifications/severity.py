from enum import Enum


class Severity(str, Enum):
    ERROR = "error"
    INFO = "info"
    WARNING = "warning"
    SUCCESS = "success"

