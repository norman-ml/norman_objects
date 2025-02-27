from datetime import datetime, timezone, timedelta

from norman_objects.norman_base_model.norman_base_model import NormanBaseModel
from norman_objects.status_flags.status_flag_value import StatusFlagValue
from pydantic import Field


class InvocationHistory(NormanBaseModel):
    id: str
    account_id: str
    model_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    flag_value: StatusFlagValue
    model_name: str
    asset_id: str
    asset_name: str
