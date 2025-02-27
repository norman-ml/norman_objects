from pydantic import BaseModel, create_model
from typing import Type, Optional

class NormanBaseModel(BaseModel):

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls.UpdateSchema: Type[BaseModel] = create_model(
            f"{cls.__name__}Update",
            **{field_name: (Optional[field_type], None) for field_name, field_type in cls.__annotations__.items()}
        )

        setattr(cls.UpdateSchema, "to_sql_fields", NormanBaseModel.to_sql_fields)

    def to_sql_fields(self):
        field_dictionary = self.dict(exclude_unset=True)
        sql_dictionary = {self.to_sql_field_name(key): value for key, value in field_dictionary.items()}
        return sql_dictionary

    def to_sql_field_name(self, field_name: str):
        split_names = field_name.split("_")
        capitalized_names = [word.capitalize() for word in split_names]
        return "_".join(capitalized_names)
