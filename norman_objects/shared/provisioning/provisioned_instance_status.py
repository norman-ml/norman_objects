from enum import Enum


class ProvisionedInstanceStatus(str, Enum):
    Pending = "Pending"
    Running = "Running"
    ShuttingDown = "ShuttingDown"
    Terminated = "Terminated"
