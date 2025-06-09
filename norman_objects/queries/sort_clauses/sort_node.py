from typing import Dict, Set

from norman_objects.queries.sort_clauses.sort_direction import SortDirection
from pydantic import BaseModel


class SortNode(BaseModel):
    table: str
    column: str
    direction: SortDirection

    def validate_expression(self, allowed_tables_and_columns: Dict[str, Set[str]]):
        if self.table not in allowed_tables_and_columns:
            return False

        if self.column not in allowed_tables_and_columns[self.table]:
            return False

        return True

    def build_expression(self):
        return f" {self.table}.{self.column} {self.direction.value} "
