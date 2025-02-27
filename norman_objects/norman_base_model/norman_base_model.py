from pydantic import BaseModel, create_model
from typing import Type, Optional

class NormanBaseModel(BaseModel):
    __field_to_sql_mapping__ = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls.UpdateSchema: Type[BaseModel] = create_model(
            f"{cls.__name__}Update",
            **{field_name: (Optional[field_type], None) for field_name, field_type in cls.__annotations__.items()}
        )

        cls.UpdateSchema.__field_to_sql_mapping__ = cls.__field_to_sql_mapping__

        setattr(cls.UpdateSchema, "to_sql_fields", NormanBaseModel.to_sql_fields)

    def to_sql_fields(self) -> dict:
        account_data = self.dict(exclude_unset=True)

        if not account_data:
            raise ValueError("No fields provided for update")

        return {self.__field_to_sql_mapping__[key]: value for key, value in account_data.items() if key in self.__field_to_sql_mapping__}
