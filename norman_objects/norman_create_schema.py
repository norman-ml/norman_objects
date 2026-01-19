from typing import ClassVar, Optional, Type

from pydantic import BaseModel


class NormanCreateSchema(BaseModel):
    def to_sql_fields(self):
        field_dictionary = self.model_dump(exclude_unset=True)
        sql_dictionary = {self.to_sql_field_name(key): value for key, value in field_dictionary.items()}
        return sql_dictionary

    def to_sql_field_name(self, field_name: str):
        split_names = field_name.split("_")
        capitalized_names = [word.capitalize() for word in split_names]
        return "_".join(capitalized_names)
