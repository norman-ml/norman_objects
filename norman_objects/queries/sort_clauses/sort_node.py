from typing import Set

from norman_objects.queries.sort_clauses.sort_direction import SortDirection
from pydantic import BaseModel


class SortNode(BaseModel):
    table: str
    column: str
    direction: SortDirection

    def validate_expression(self, allowed_tables: Set[str], allowed_columns: Set[str]):
        table_valid = self.table in allowed_tables
        column_valid = self.column in allowed_columns

        return table_valid and column_valid

    def build_expression(self):
        return f" {self.table}.{self.column} {self.direction.value} "
