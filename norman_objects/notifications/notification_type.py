from enum import Enum


class NotificationType(str, Enum):
    Model = "Model"
    Invocation = "Invocation"

