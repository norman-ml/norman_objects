from datetime import datetime, timezone
from pydantic import BaseModel, create_model, field_validator, field_serializer, ConfigDict
from typing import Type, Optional, Any
from norman_objects.norman_update_schema import NormanUpdateSchema
from norman_objects.shared.security.sensitive import Sensitive


class NormanBaseModel(BaseModel):
    model_config = ConfigDict(
        json_encoders={
            Sensitive: lambda v: str(v)
        },
        arbitrary_types_allowed=True,
    )

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


    @field_validator("*", mode="after")
    @classmethod
    def _normalize_datetime(cls, value: Any):
        if isinstance(value, datetime) and value.tzinfo is None:
            value = value.astimezone(timezone.utc)
        return value


    @field_serializer("*", when_used="json")
    def _serialize_datetime(self, value: Any):
        if isinstance(value, datetime) and value.tzinfo is None:
            value = value.astimezone(timezone.utc)
        return value
    