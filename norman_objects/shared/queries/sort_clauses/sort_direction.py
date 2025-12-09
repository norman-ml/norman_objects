from enum import Enum


class SortDirection(str, Enum):
    """
    Sort direction enum used to specify ascending or descending order.

    **Values**

    - **ASC** - Sort in ascending order
    - **DESC** - Sort in descending order
    """
    ASC = "ASC"
    DESC = "DESC"

