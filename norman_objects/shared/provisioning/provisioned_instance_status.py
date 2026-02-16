from enum import Enum


class ProvisionedInstanceStatus(str, Enum):
    Down = "Down"
    Up = "Up"
