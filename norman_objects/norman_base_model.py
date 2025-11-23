from datetime import datetime, timezone
from pydantic import BaseModel, create_model, field_validator, field_serializer, SerializerFunctionWrapHandler, ValidatorFunctionWrapHandler
from typing import Type, Optional, Any
from norman_objects.norman_update_schema import NormanUpdateSchema


class NormanBaseModel(BaseModel):
    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs):
        cls.UpdateSchema: Type[BaseModel] = create_model(
            f"{cls.__name__}Update",
            **{
                name: (Optional[field.annotation], None)
                for name, field in cls.model_fields.items()
            },
            __base__=NormanUpdateSchema,
        )


    @field_validator("*", mode="wrap")
    @classmethod
    def _normalize_datetime(cls, value: Any, handler: ValidatorFunctionWrapHandler):
        value = handler(value)
        if isinstance(value, datetime) and value.tzinfo is None:
            value = value.astimezone(timezone.utc)

        return value


    @field_serializer("*", mode="wrap", when_used="always")
    def _serialize_datetime(self, value: Any, handler: SerializerFunctionWrapHandler):
        if isinstance(value, datetime) and value.tzinfo is None:
            value = value.astimezone(timezone.utc)

        return handler(value)
    