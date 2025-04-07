from typing import Optional

from norman_objects.queries.parameterization_type import ParameterizationType
from pydantic import BaseModel


class PageClause(BaseModel):
    limit: Optional[int]
    offset: Optional[int]

    def validate_expression(self):
        return (
            self.limit is None or self.limit >= 0
            and
            self.offset is None or self.offset >= 0
        )

    def build_expression(self, parameterization_type):
        if parameterization_type == ParameterizationType.LIST_BASED:
            clause, parameters = self.build_expression_as_list()
        elif parameterization_type == ParameterizationType.DICT_BASED:
            clause, parameters = self.build_expression_as_dict()
        else:
            raise ValueError(f"Unsupported parameterization type")

        return clause, parameters

    def build_expression_as_list(self):
        clause = ""
        parameters = []

        if self.limit is not None:
            clause += " LIMIT %s "
            parameters.append(self.limit)

        if self.offset is not None:
            clause += " OFFSET %s "
            parameters.append(self.offset)

        return clause, parameters

    def build_expression_as_dict(self):
        clause = ""
        parameters = {}

        if self.limit is not None:
            clause += " LIMIT %(limit)s "
            parameters["limit"] = self.limit

        if self.offset is not None:
            clause += " OFFSET %(offset)s "
            parameters["offset"] = self.offset

        return clause, parameters
