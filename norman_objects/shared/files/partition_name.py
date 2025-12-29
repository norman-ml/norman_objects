from enum import Enum


class PartitionName(str, Enum):
    Build = "Build"
    Ephemeral = "Ephemeral"
    Permanent = "Permanent"
