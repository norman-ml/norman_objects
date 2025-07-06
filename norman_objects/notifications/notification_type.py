from enum import Enum


class NotificationType(str, Enum):
    Invocation = "Invocation"
    Model = "Model"

