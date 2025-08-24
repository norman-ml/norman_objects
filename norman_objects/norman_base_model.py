from typing import Type, Optional
from pydantic import BaseModel, create_model, model_validator
from pydantic.fields import FieldInfo

from norman_objects.norman_update_schema import NormanUpdateSchema
from norman_objects.sensitive.sensitive import Sensitive


class NormanBaseModel(BaseModel):

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls.UpdateSchema: Type[BaseModel] = create_model(
            f"{cls.__name__}Update",
            **{
                name: (Optional[field.annotation], None)
                for name, field in cls.model_fields.items()
            },
            __base__=NormanUpdateSchema
        )

        cls._sensitive_fields = {
            field_name: field.annotation
            for field_name, field in cls.model_fields.items()
            if isinstance(field.annotation, type)
                and issubclass(field.annotation, Sensitive)
        }

    def validate_sensitive_fields(self):
        for field_name, field_type in self._sensitive_fields.items():
            value = getattr(self, field_name, None)
            if value is not None and not isinstance(value, field_type):
                setattr(self, field_name, field_type(value))

    @model_validator(mode="after")
    def run_validation(self):
        self.validate_sensitive_fields()
        return self
