from enum import Enum
from functools import total_ordering


@total_ordering
class StatusFlagValue(int, Enum):
    Not_Started = 0
    Enqueued = 1
    In_Progress = 2
    Finished = 3
    Error = 4

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
