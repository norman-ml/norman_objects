from typing import Type, Optional

from pydantic import BaseModel, ConfigDict, create_model

from norman_objects.norman_update_schema import NormanUpdateSchema


class NormanBaseModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

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
    