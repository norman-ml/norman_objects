from typing import Dict, Set

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.queries.sort_clauses.sort_direction import SortDirection


class SortNode(NormanBaseModel):
    table: str
    column: str = "ID"
    direction: SortDirection = SortDirection.ASC

    def validate_expression(self, allowed_tables_and_columns: Dict[str, Set[str]]):
        if self.table not in allowed_tables_and_columns:
            return False

        if self.column not in allowed_tables_and_columns[self.table]:
            return False

        return True

    def build_expression(self):
        return f" {self.table}.{self.column} {self.direction.value} "