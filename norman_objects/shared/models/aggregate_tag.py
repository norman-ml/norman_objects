from typing import Annotated

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.hydration.id_markers import DerivedId


class AggregateTag(NormanBaseModel):
    model_id: Annotated[str, DerivedId("model_id")]
    name: str
    tag_count: int
