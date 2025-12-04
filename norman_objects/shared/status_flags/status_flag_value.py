from enum import Enum
from functools import total_ordering


@total_ordering
class StatusFlagValue(int, Enum):
    """
    Represents the progress state of a workflow step.

    Values are ordered so they can be compared (e.g., to determine
    forward progress), thanks to the `@total_ordering` decorator.

    **Values**

    - **Not_Started** (`0`)
      Step has not begun yet.

    - **Enqueued** (`1`)
      Step is queued but not yet started.

    - **In_Progress** (`2`)
      Step is currently running.

    - **Finished** (`3`)
      Step completed successfully.

    - **Error** (`4`)
      Step failed or encountered an unrecoverable issue.
    """
    Not_Started = 0
    Enqueued   = 1
    In_Progress = 2
    Finished   = 3
    Error      = 4


    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
