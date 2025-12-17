from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class InvocationHistory(NormanBaseModel):
    id: str
    account_id: str
    model_id: str
    version_id: str
    asset_id: str
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
    model_name: str
    flag_value: StatusFlagValue
