from datetime import datetime, timedelta, timezone
from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from pydantic import Field, EmailStr


class AccountProfile(NormanBaseModel):
    account_id: str
    name: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    email: Optional[EmailStr] = None
