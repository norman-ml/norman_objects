from enum import Enum


class ModelBuildStatus(str, Enum):
    InProgress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
