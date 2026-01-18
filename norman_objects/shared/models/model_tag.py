from typing import Annotated

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.hydration import GeneratedId, DerivedId


class ModelTag(NormanBaseModel):
    id: Annotated[str, GeneratedId()]
    account_id: str = ""
    model_id: Annotated[str, DerivedId("model_id")]
    name: str
