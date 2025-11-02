from datetime import datetime, timezone
from typing import Type, Optional, Any

from pydantic import BaseModel, create_model, field_validator

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

    @field_validator("*", mode='after')
    @classmethod
    def _normalize_datetime(cls, value: Any):
        if isinstance(value, datetime):
            if value.tzinfo is None:
                value = value.replace(tzinfo=timezone.utc)

        return value
