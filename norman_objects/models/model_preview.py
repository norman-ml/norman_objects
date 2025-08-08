from pydantic import Field
from datetime import datetime, timezone, timedelta

from norman_objects.models.model_asset import ModelAsset
from norman_objects.norman_base_model import NormanBaseModel

class ModelPreview(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_base_id: str = "0"
    version_label: str
    active: bool = True
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    short_description: str
    assets: list[ModelAsset] = []
