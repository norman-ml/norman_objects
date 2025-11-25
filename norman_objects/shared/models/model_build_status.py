#TODO - this is step 1: creating an enum
from enum import Enum

class ModelBuildStatus(str, Enum):
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
