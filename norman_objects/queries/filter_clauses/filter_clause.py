from typing import Dict, List, Union, Set

from norman_objects.queries.filter_clauses.filter_node import FilterNode
from norman_objects.queries.logical_relations.binary_relation import BinaryRelation
from norman_objects.queries.logical_relations.unary_relation import UnaryRelation
from norman_objects.queries.parameterization_type import ParameterizationType
from norman_objects.queries.transforms.constraint_transform import ConstraintTransform
from pydantic import BaseModel


class FilterClause(BaseModel):
    children: List[Union["FilterClause", FilterNode]]
    join_condition: UnaryRelation = UnaryRelation.AND

    @classmethod
    def equals(cls, table: str, column: str = "ID", value: Union[str, int, float] = None):
        return cls.with_filter(
            table=table,
            column=column,
            operator=BinaryRelation.EQ,
            value=value,
            join_condition=UnaryRelation.AND
        )

    @classmethod
    def includes(cls, table: str, column: str = "ID", value: List[Union[str, int, float]] = None):
        if len(value) <= 0:
            raise ValueError("Filter clause value cannot be an empty list")
        return cls.with_filter(
            table=table,
            column=column,
            operator=BinaryRelation.IN,
            value=value,
            join_condition=UnaryRelation.OR
        )

    @classmethod
    def not_includes(cls, table: str, column: str = "ID", value: List[Union[str, int, float]] = None):
        if len(value) <= 0:
            raise ValueError("Filter clause value cannot be an empty list")

        return cls.with_filter(
            table=table,
            column=column,
            operator=BinaryRelation.NIN,
            value=value,
            join_condition=UnaryRelation.OR
        )

    @classmethod
    def with_filter(cls, table: str, column: str = "ID", operator: BinaryRelation = BinaryRelation.EQ, value: Union[str, List[Union[str, int, float]]] = None, join_condition: UnaryRelation = UnaryRelation.AND):
        if value is None:
            raise ValueError("Filter clause value cannot be None")

        return cls(
            children=[
                FilterNode(
                    table=table,
                    column=column,
                    operator=operator,
                    value=value
                )
            ],
            join_condition = join_condition
        )


    def __and__(self, other):
        if not isinstance(other, FilterClause):
            raise ValueError("Logical AND is only supported between two filter clauses")

        return FilterClause(
            children = [*self.children, *other.children],
            join_condition = self.join_condition
        )

    def validate_expression(self, allowed_tables_and_columns: Dict[str, Set[str]]):
        for child_node in self.children:
            if not child_node.validate_expression(allowed_tables_and_columns):
                return False

        return True

    def build_expression(self, parameterization_type: ParameterizationType, transforms: List[ConstraintTransform] = None):
        if parameterization_type == ParameterizationType.LIST_BASED:
            clause, parameters = self.build_expression_as_list(parameterization_type, transforms)
        elif parameterization_type == ParameterizationType.DICT_BASED:
            clause, parameters = self.build_expression_as_dict(parameterization_type, transforms)
        else:
            raise ValueError("Unsupported parameterization type")

        return clause, parameters

    def build_expression_as_list(self, parameterization_type: ParameterizationType, transforms: List[ConstraintTransform] = None):
        clauses = []
        parameters = []

        for branch in self.children:
            branch_clause, branch_parameters = branch.build_expression(parameterization_type, transforms)
            clauses.append(f" ({branch_clause}) ")
            parameters += branch_parameters

        joint_expression = f" {self.join_condition.value} ".join(clauses)
        return joint_expression, parameters

    def build_expression_as_dict(self, parameterization_type: ParameterizationType, transforms: List[ConstraintTransform] = None):
        clauses = []
        parameters = {}

        for branch in self.children:
            branch_clause, branch_parameters = branch.build_expression(parameterization_type, transforms)
            clauses.append(f" ({branch_clause}) ")
            parameters |= branch_parameters

        joint_expression = f" {self.join_condition.value} ".join(clauses)
        return joint_expression, parameters
