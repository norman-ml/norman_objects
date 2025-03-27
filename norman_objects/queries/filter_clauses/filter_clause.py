from typing import List, Union, Set

from norman_objects.queries.filter_clauses.filter_node import FilterNode
from norman_objects.queries.logical_relations.unary_relation import UnaryRelation
from norman_objects.queries.parameterization_type import ParameterizationType
from norman_objects.queries.transforms.constraint_transform import ConstraintTransform
from pydantic import BaseModel


class FilterClause(BaseModel):
    join_condition: UnaryRelation
    children: List[Union["FilterClause", FilterNode]]

    def validate_columns(self, allowed_columns: Set[str]):
        for child_node in self.children:
            if not child_node.validate_columns(allowed_columns):
                return False

        return True

    def build_expression(self, parameterization_type: ParameterizationType, transforms: List[ConstraintTransform]):
        if parameterization_type == ParameterizationType.LIST_BASED:
            clause, parameters = self.build_expression_as_list(parameterization_type, transforms)
        elif parameterization_type == ParameterizationType.DICT_BASED:
            clause, parameters = self.build_expression_as_dict(parameterization_type, transforms)
        else:
            raise ValueError(f"Unsupported parameterization type")

        return clause, parameters

    def build_expression_as_list(self, parameterization_type: ParameterizationType, transforms: List[ConstraintTransform]):
        clauses = []
        parameters = []

        for branch in self.children:
            branch_clause, branch_parameters = branch.build_expression(parameterization_type, transforms)
            clauses.append(f" ({branch_clause}) ")
            parameters += branch_parameters

        joint_expression = f" {self.join_condition.value} ".join(clauses)
        return joint_expression, parameters

    def build_expression_as_dict(self, parameterization_type: ParameterizationType, transforms: List[ConstraintTransform]):
        clauses = []
        parameters = {}

        for branch in self.children:
            branch_clause, branch_parameters = branch.build_expression(parameterization_type, transforms)
            clauses.append(f" ({branch_clause}) ")
            parameters |= branch_parameters

        joint_expression = f" {self.join_condition.value} ".join(clauses)
        return joint_expression, parameters
