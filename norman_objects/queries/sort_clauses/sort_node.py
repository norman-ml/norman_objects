from typing import Dict, Set, Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.queries.sort_clauses.sort_direction import SortDirection


class SortNode(NormanBaseModel):
    table: Optional[str] = None
    column: str = "ID"
    direction: SortDirection = SortDirection.ASC

    def validate_expression(self, allowed_tables_and_columns: Dict[str, Set[str]]):
        if self.column not in allowed_tables_and_columns[self.table]:
            return False

        if self.table is None:
            return True

        if self.table not in allowed_tables_and_columns:
            return False

        return True

    def build_expression(self):
        if self.table is None:
            return f" {self.column} {self.direction.value} "
        else:
            return f" {self.table}.{self.column} {self.direction.value} "
