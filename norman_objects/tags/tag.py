from datetime import datetime, timezone, timedelta
from pydantic import BaseModel, Field

class Tag(BaseModel):
    id: str
    name: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
