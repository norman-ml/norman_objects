from typing import Dict, List, Set

from norman_objects.queries.sort_clauses.sort_node import SortNode
from pydantic import BaseModel


class SortClause(BaseModel):
    children: List[SortNode]

    def __and__(self, other):
        if not isinstance(other, SortClause):
            raise ValueError("Logical AND is only supported between two sort clauses")

        return SortClause(
            children=[*self.children, *other.children]
        )

    def validate_expression(self, allowed_tables_and_columns: Dict[str, Set[str]]):
        for child_node in self.children:
            if not child_node.validate_expression(allowed_tables_and_columns):
                return False

        return True

    def build_expression(self):
        ordering = []
        for sort_node in self.children:
            expression = sort_node.build_expression()
            ordering.append(expression)

        order_by_sql = ", ".join(ordering)
        return order_by_sql
