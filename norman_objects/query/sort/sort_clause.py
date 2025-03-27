from typing import List, Set

from norman_objects.query.sort.sort_node import SortNode
from pydantic import BaseModel


class SortClause(BaseModel):
    children: List[SortNode]

    def validate_columns(self, allowed_columns: Set[str]):
        for child_node in self.children:
            if not child_node.validate_columns(allowed_columns):
                return False

        return True

    def build_expression(self):
        ordering = []
        for sort_node in self.children:
            expression = sort_node.build_expression()
            ordering.append(expression)

        order_by_sql = ", ".join(ordering)
        return order_by_sql
