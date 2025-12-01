from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.models.model_preview import ModelPreview
from norman_objects.shared.tags.aggregate_tag import AggregateTag
from norman_objects.shared.tags.model_base_tag import ModelBaseTag


class ModelBase(NormanBaseModel):
    id: str
    account_id: str
    name: str
    invocation_count: int
    model_previews: list[ModelPreview] = []
    tags: list[AggregateTag] = []
    user_added_tags: list[ModelBaseTag] = []
