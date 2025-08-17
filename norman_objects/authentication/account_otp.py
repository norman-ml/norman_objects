
from datetime import datetime, timedelta, timezone

from norman_objects.norman_base_model import NormanBaseModel
from pydantic import Field


class AccountOTP(NormanBaseModel):
    id: str = "0"
    account_id: str
    credential_hash_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    verified: bool = False
