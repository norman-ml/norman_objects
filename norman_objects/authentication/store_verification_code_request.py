from datetime import datetime, timedelta, timezone

from norman_objects.norman_base_model import NormanBaseModel
from pydantic import Field


class StoreVerificationCodeRequest(NormanBaseModel):
    account_id: str
    email: str
    code: str
    expiration_time: datetime
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))

