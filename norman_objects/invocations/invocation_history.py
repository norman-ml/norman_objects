from datetime import datetime, timezone, timedelta
from pydantic import BaseModel, Field


class InvocationHistory(BaseModel):
    id: str
    model_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    flag_name: str
    model_name: str
    asset_id: str
    asset_name: str
