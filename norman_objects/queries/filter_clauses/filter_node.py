from typing import Dict, List, Union, Set

from norman_objects.queries.logical_relations.binary_relation import BinaryRelation
from norman_objects.queries.parameterization_type import ParameterizationType
from norman_objects.queries.transforms.constraint_transform import ConstraintTransform
from pydantic import BaseModel


class FilterNode(BaseModel):
    table: str
    column: str = "ID"
    operator: BinaryRelation = BinaryRelation.EQ
    value: Union[str, List[Union[str, int, float]]]

    def validate_expression(self, allowed_tables_and_columns: Dict[str, Set[str]]):
        if self.table not in allowed_tables_and_columns:
            return False

        if self.column not in allowed_tables_and_columns[self.table]:
            return False

        if not self.validate_type():
            return False

        return True

    def validate_table(self, allowed_tables: Set[str]):
        return self.table in allowed_tables

    def validate_column(self, allowed_columns: Set[str]):
        return self.column in allowed_columns

    def validate_type(self):
        if self.operator in (BinaryRelation.IN, BinaryRelation.NIN):
            return isinstance(self.value, list)
        return isinstance(self.value, (str, int, float))

    def build_expression(self, parameterization_type: ParameterizationType, transforms: List[ConstraintTransform] = None):
        if parameterization_type == ParameterizationType.LIST_BASED:
            clause, parameters = self.build_expression_as_list(transforms)
        elif parameterization_type == ParameterizationType.DICT_BASED:
            clause, parameters = self.build_expression_as_dict(transforms)
        else:
            raise ValueError("Unsupported parameterization type")

        return clause, parameters

    def build_expression_as_list(self, transforms: List[ConstraintTransform] = None):
        if self.operator == BinaryRelation.IN or self.operator == BinaryRelation.NIN:
            collection_placeholders = ["%s"] * len(self.value)
            interpolation_placeholder = f"({', '.join(collection_placeholders)})"

            transformed_values = self.transform(transforms)
            parameters = transformed_values

        else:
            interpolation_placeholder = " %s "
            transformed_value = self.transform(transforms)
            parameters = [transformed_value]

        clause = f" {self.table}.{self.column} {self.operator.value} {interpolation_placeholder} "
        return clause, parameters

    def build_expression_as_dict(self, transforms: List[ConstraintTransform] = None):
        if self.operator == BinaryRelation.IN or self.operator == BinaryRelation.NIN:
            raise ValueError("Collection operators not supported with dict parameterization")

        interpolation_placeholder = f" %({self.table}.{self.column})s "
        clause = f" {self.table}.{self.column} {self.operator.value} {interpolation_placeholder} "

        transformed_value = self.transform(transforms)
        parameters = {
            f"{self.table}.{self.column}": transformed_value
        }

        return clause, parameters

    def transform(self, transforms: List[ConstraintTransform] = None):
        if transforms is None:
            return self.value

        for transform in transforms:
            if transform.column_name == self.column:
                if isinstance(self.value, list):
                    return [transform.function(v) for v in self.value]
                return transform.function(self.value)

        return self.value
