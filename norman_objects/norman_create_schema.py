from typing import ClassVar, Optional, Type

from pydantic import BaseModel


class NormanCreateSchema(BaseModel):
    """
    Base class for auto-generated CreateSchema variants.

    CreateSchema instances have a _norman_full_model_class attribute
    that points back to the original model class, enabling hydration.
    """
    _norman_full_model_class: ClassVar[Optional[Type[BaseModel]]] = None

    class Config:
        # Allow extra attributes for the class-level _norman_full_model_class
        extra = "forbid"
