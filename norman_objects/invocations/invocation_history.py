from datetime import datetime, timezone, timedelta
from pydantic import BaseModel, Field
from norman_objects.status_flags.status_flag_value import StatusFlagValue


class InvocationHistory(BaseModel):
    id: str
    account_id: str
    model_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    flag_value: StatusFlagValue
    model_name: str
    asset_id: str
    asset_name: str
