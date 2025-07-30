from typing import Dict, List, Optional, Set, Union

from norman_objects.queries.filter_clauses.filter_clause import FilterClause
from norman_objects.queries.logical_relations.binary_relation import BinaryRelation
from norman_objects.queries.logical_relations.unary_relation import UnaryRelation
from norman_objects.queries.page_clauses.page_clause import PageClause
from norman_objects.queries.parameterization_type import ParameterizationType
from norman_objects.queries.sort_clauses.sort_clause import SortClause
from norman_objects.queries.transforms.constraint_transform import ConstraintTransform
from pydantic import BaseModel


class QueryConstraints(BaseModel):
    filter: Optional[FilterClause] = None
    sort: Optional[SortClause] = None
    page: Optional[PageClause] = None

    @classmethod
    def equals(cls, table: str, column: str = "ID", value = None):
        return cls(
            filter=FilterClause.equals(table, column, value)
        )

    @classmethod
    def includes(cls, table: str, column: str = "ID", value: List[Union[str, int, float]] = None):
        return cls(
            filter=FilterClause.includes(table, column, value)
        )

    @classmethod
    def not_includes(cls, table: str, column: str = "ID", value: List[Union[str, int, float]] = None):
        return cls(
            filter=FilterClause.not_includes(table, column, value)
        )

    @classmethod
    def with_filter(cls, table: str, column: str = "ID", operator: BinaryRelation = BinaryRelation.EQ,
                    value: Union[str | List[Union[str, int, float]]] = None, join_condition: UnaryRelation = UnaryRelation.AND):
        return cls(
            filter=FilterClause.with_filter(table, column, operator, value, join_condition)
        )

    def __and__(self, other):
        if not isinstance(other, QueryConstraints):
            raise ValueError("Logical AND is only supported between two query constraints")

        combined_filter = FilterClause(
            children = [],
            join_condition = UnaryRelation.AND
        )

        if self.filter is not None:
            combined_filter.children.append(self.filter)
        if other.filter is not None:
            combined_filter.children.append(other.filter)

        if self.sort is not None and other.sort is not None:
            combined_sort = self.sort & other.sort
        elif other.sort is None:
            combined_sort = self.sort
        else:
            combined_sort = other.sort

        if other.page is None:
            combined_page = self.page
        else:
            combined_page = other.page

        return QueryConstraints(
            filter=combined_filter,
            sort=combined_sort,
            page=combined_page
        )

    def validate_expression(self, allowed_tables_and_columns: Dict[str, Set[str]]):
        constraint_valid = True

        if self.filter is not None:
            filter_valid = self.filter.validate_expression(allowed_tables_and_columns)
            constraint_valid = constraint_valid and filter_valid

        if self.sort is not None:
            sort_valid = self.sort.validate_expression(allowed_tables_and_columns)
            constraint_valid = constraint_valid and sort_valid

        if self.page is not None:
            page_valid = self.page.validate_expression()
            constraint_valid = constraint_valid and page_valid

        if not constraint_valid:
            raise ValueError("Invalid column names in constraints.")

    def build_expression(self, base_query: str, parameterization_type: ParameterizationType, transforms: List[ConstraintTransform] = None):
        if parameterization_type == ParameterizationType.LIST_BASED:
            clause, parameters = self.build_expression_as_list(parameterization_type, transforms)
        elif parameterization_type == ParameterizationType.DICT_BASED:
            clause, parameters = self.build_expression_as_dict(parameterization_type, transforms)
        else:
            raise ValueError("Unsupported parameterization type")

        joint_query = f" {base_query} {clause} "
        return joint_query, parameters

    def build_expression_as_list(self, parameterization_type: ParameterizationType, transforms: List[ConstraintTransform] = None):
        child_clauses = []
        child_parameters = []

        if self.filter is not None and len(self.filter.children) > 0:
            filter_clause, filter_parameters = self.filter.build_expression(parameterization_type, transforms)
            child_clauses.append(f" WHERE {filter_clause} ")
            child_parameters += filter_parameters

        if self.sort is not None:
            sort_clause = self.sort.build_expression()
            child_clauses.append(f" ORDER BY {sort_clause} ")

        if self.page is not None:
            paging_clause, paging_parameters = self.page.build_expression(parameterization_type)
            child_clauses.append(paging_clause)
            child_parameters += paging_parameters

        clause = " ".join(child_clauses)
        return clause, child_parameters

    def build_expression_as_dict(self, parameterization_type: ParameterizationType, transforms: List[ConstraintTransform] = None):
        child_clauses = []
        child_parameters = {}

        if self.filter is not None and len(self.filter.children) > 0:
            filter_clause, filter_parameters = self.filter.build_expression(parameterization_type, transforms)
            child_clauses.append(f" WHERE {filter_clause} ")
            child_parameters |= filter_parameters

        if self.sort is not None:
            sort_clause = self.sort.build_expression()
            child_clauses.append(f" ORDER BY {sort_clause} ")

        if self.page is not None:
            paging_clause, paging_parameters = self.page.build_expression(parameterization_type)
            child_clauses.append(paging_clause)
            child_parameters |= paging_parameters

        clause = " ".join(child_clauses)
        return clause, child_parameters
