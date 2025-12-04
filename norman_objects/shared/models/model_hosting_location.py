from enum import Enum


class ModelHostingLocation(str, Enum):
    """
    Indicates where a model is physically hosted.

    **Values**

    - **External** — Model hosted outside the Norman platform.
    - **Internal** — Model hosted within the Norman infrastructure.
    """
    External = "External"
    Internal = "Internal"
