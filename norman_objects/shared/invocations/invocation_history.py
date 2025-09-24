from datetime import datetime, timezone, timedelta

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.status_flags.status_flag_name import StatusFlagName
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class InvocationHistory(NormanBaseModel):
    id: str
    account_id: str
    model_id: str
    asset_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    model_name: str
    entity_id: str
    flag_name: StatusFlagName
    flag_value: StatusFlagValue
