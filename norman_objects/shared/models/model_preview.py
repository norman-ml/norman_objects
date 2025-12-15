from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.models.aggregate_tag import AggregateTag
from norman_objects.shared.models.model_version_preview import ModelVersionPreview


class ModelPreview(NormanBaseModel):
    id: str
    account_id: str

    name: str
    invocation_count: int

    versions: list[ModelVersionPreview] = []
    aggregate_tags: list[AggregateTag] = []
