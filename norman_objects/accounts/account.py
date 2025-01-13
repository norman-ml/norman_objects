from datetime import datetime, timedelta, timezone
from typing import Optional

from pydantic import BaseModel, Field

class Account(BaseModel):
    id: str = "0"
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    name: str
    email: Optional[str] = None
