from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class Account(NormanBaseModel):
    id: str = "0"
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
    name: str
