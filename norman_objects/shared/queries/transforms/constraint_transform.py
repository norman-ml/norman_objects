from typing import Callable


class ConstraintTransform:
    def __init__(self, column_name: str, function: Callable):
        self.column_name = column_name
        self.function = function
