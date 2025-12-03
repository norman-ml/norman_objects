from enum import Enum


class ModelBuildStatus(str, Enum):
    In_progress = "InProgress"
    Completed = "Completed"
    Failed = "Failed"
