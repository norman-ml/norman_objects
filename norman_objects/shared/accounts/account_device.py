from datetime import datetime, timezone, timedelta

from norman_objects.norman_base_model import NormanBaseModel
from pydantic import Field


class AccountDevice(NormanBaseModel):
    id: str = "0"
    account_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
