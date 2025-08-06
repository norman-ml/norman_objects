from datetime import datetime, timedelta, timezone
from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from pydantic import Field


class Account(NormanBaseModel):
    id: str = "0"
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    name: str
    email: Optional[str] = None
    registered: int
    confirmed: int
