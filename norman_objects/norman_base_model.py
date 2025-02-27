from pydantic import BaseModel, create_model
from typing import Type, Optional

from norman_objects.norman_update_schema import NormanUpdateSchema


class NormanBaseModel(BaseModel):

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls.UpdateSchema: Type[BaseModel] = create_model(
            f"{cls.__name__}Update",
            **{field_name: (Optional[field_type], None) for field_name, field_type in cls.__annotations__.items()},
            __base__ = NormanUpdateSchema
        )
