from datetime import datetime, timedelta, timezone
from typing import Optional

from pydantic import BaseModel, Field
from norman_objects.notifications.severity import Severity

class InvocationNotification(BaseModel):
    id: str = None
    account_id: str = None
    entity_id: str = None
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    model_name: Optional[str] = None
    title: str
    message: str
    read_status: int
    severity: Severity
