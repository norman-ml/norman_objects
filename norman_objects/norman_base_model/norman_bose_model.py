from typing import Type, Optional
from pydantic import BaseModel, create_model


class NormanBaseModel(BaseModel):
    def __init_subclass__ (cls, **kwargs):
        super().__init_subclass__ (**kwargs)

        cls.UpdateSchema: Type[BaseModel] = create_model(
            f"{cls.__name__}Update",
            **{field_name: (Optional[field_type], None) for field_name, field_type in cls.__annotations__.items()}
        )
