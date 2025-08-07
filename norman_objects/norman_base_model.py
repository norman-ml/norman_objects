from pydantic import BaseModel, create_model, root_validator
from typing import Type, Optional

from norman_objects.norman_update_schema import NormanUpdateSchema
from norman_objects.sensitive.sensitive import Sensitive


class NormanBaseModel(BaseModel):

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls.UpdateSchema: Type[BaseModel] = create_model(
            f"{cls.__name__}Update",
            **{field.name: (Optional[field.type_], None) for field in cls.__fields__.values()},
            __base__=NormanUpdateSchema
        )

        cls._sensitive_fields = {
            field_name: model_field.type_
            for field_name, model_field in cls.__fields__.items()
            if isinstance(model_field.type_, type)
                and issubclass(model_field.type_, Sensitive)
        }

    @root_validator(pre=True)
    def wrap_sensitive_fields(cls, values):
        for field_name, field_type in cls._sensitive_fields.items():
            value = values.get(field_name)
            if value is not None and not isinstance(value, field_type):
                values[field_name] = field_type(value)
        return values
