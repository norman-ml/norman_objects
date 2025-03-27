from typing import Set

from norman_objects.query.sort.sort_direction import SortDirection
from pydantic import BaseModel


class SortNode(BaseModel):
    column: str
    direction: SortDirection

    def validate_columns(self, allowed_columns: Set[str]):
        return self.column in allowed_columns

    def build_expression(self):
        return f" {self.column} {self.direction.value} "
