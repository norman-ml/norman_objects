from datetime import datetime, timezone
from typing import Optional

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.models.aggregate_tag import AggregateTag
from norman_objects.shared.models.model_asset import ModelAsset
from norman_objects.shared.models.model_build_status import ModelBuildStatus


class ModelPreview(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_base_id: str = "0"
    version_label: str
    active: bool = True
    build_status: Optional[ModelBuildStatus] = None
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
    short_description: str

    assets: list[ModelAsset] = []
    tags: list[AggregateTag] = []
