from datetime import datetime, timezone, timedelta

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.models.aggregate_tag import AggregateTag
from norman_objects.shared.models.model_asset import ModelAsset


class ModelPreview(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_base_id: str = "0"
    version_label: str
    active: bool = True
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    short_description: str

    assets: list[ModelAsset] = []
    tags: list[AggregateTag] = []
