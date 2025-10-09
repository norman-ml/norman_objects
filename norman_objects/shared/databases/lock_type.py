from enum import Enum


class LockType(str, Enum):
    Read = "Read"
    Write = "Write"
