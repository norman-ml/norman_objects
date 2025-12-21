from typing import Collection

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.queries.filter_clauses.filter_value_type import FilterTypeVar
from norman_objects.shared.queries.logical_relations.binary_relation import BinaryRelation
from norman_objects.shared.queries.parameterization_type import ParameterizationType
from norman_objects.shared.queries.transforms.constraint_transform import ConstraintTransform


class FilterNode(NormanBaseModel):
    table: str
    column: str = "ID"
    operator: BinaryRelation = BinaryRelation.EQ
    value: FilterTypeVar

    def validate_expression(self, allowed_tables_and_columns: dict[str, set[str]]):
        if self.table not in allowed_tables_and_columns:
            return False

        if self.column not in allowed_tables_and_columns[self.table]:
            return False

        if not self.validate_type():
            return False

        return True

    def validate_type(self):
        if self.operator in (BinaryRelation.IN, BinaryRelation.NIN):
            return isinstance(self.value, (list, set, tuple))
        return isinstance(self.value, (str, int, float))

    def build_expression(self, parameterization_type: ParameterizationType, transforms: Collection[ConstraintTransform] = None):
        if parameterization_type == ParameterizationType.LIST_BASED:
            clause, parameters = self.build_expression_as_list(transforms)
        elif parameterization_type == ParameterizationType.DICT_BASED:
            clause, parameters = self.build_expression_as_dict(transforms)
        else:
            raise ValueError("Unsupported parameterization type")

        return clause, parameters

    def build_expression_as_list(self, transforms: Collection[ConstraintTransform] = None):
        if self.operator == BinaryRelation.IN or self.operator == BinaryRelation.NIN:
            if len(self.value) == 0:
                if self.operator == BinaryRelation.IN:
                    # Empty IN = no matches
                    return " 1 = 0 ", []
                else:
                    # Empty NOT IN = always true
                    return " 1 = 1 ", []

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

    def build_expression_as_dict(self, transforms: Collection[ConstraintTransform] = None):
        if self.operator == BinaryRelation.IN or self.operator == BinaryRelation.NIN:
            raise ValueError("Collection operators not supported with dict parameterization")

        interpolation_placeholder = f" %({self.table}.{self.column})s "
        clause = f" {self.table}.{self.column} {self.operator.value} {interpolation_placeholder} "

        transformed_value = self.transform(transforms)
        parameters = {
            f"{self.table}.{self.column}": transformed_value
        }

        return clause, parameters

    def transform(self, transforms: Collection[ConstraintTransform] = None):
        if transforms is None:
            return self.value

        for transform in transforms:
            if transform.column_name == self.column:
                if isinstance(self.value, (list, set, tuple)):
                    return [transform.function(v) for v in self.value]
                return transform.function(self.value)

        return self.value
