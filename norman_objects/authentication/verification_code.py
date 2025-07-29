from datetime import datetime, timedelta, timezone

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType
from pydantic import Field


class VerificationCode(NormanBaseModel):
    id: str = "0"
    account_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    email: str
    code: SensitiveType(str)
    expiration: datetime
    verified: int = 0
