from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.queries.sort_clauses.sort_direction import SortDirection


class SortNode(NormanBaseModel):
    """
    Single sort instruction specifying how to order records based on a
    particular column and sort direction.

    **Fields**

    - **table** (`str`)
      Table or entity name used for sorting.

    - **column** (`str`)
      Column name to sort by. Defaults to `"ID"`.

    - **direction** (`SortDirection`)
      Direction of sorting:
      - `SortDirection.ASC`
      - `SortDirection.DESC`
    """
    table: str
    column: str = "ID"
    direction: SortDirection = SortDirection.ASC


    def validate_expression(self, allowed_tables_and_columns: dict[str, set[str]]):
        if self.table not in allowed_tables_and_columns:
            return False

        if self.column not in allowed_tables_and_columns[self.table]:
            return False

        return True

    def build_expression(self):
        return f" {self.table}.{self.column} {self.direction.value} "
