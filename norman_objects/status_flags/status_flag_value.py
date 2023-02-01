from enum import Enum
from functools import total_ordering


@total_ordering
class StatusFlagValue(str, Enum):
    Error = -1
    Not_Started = 1
    Enqueued = 2
    In_Progress = 3
    Finished = 4

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
