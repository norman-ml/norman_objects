from datetime import datetime, timezone, timedelta
from pydantic import BaseModel, Field
from norman_objects.notifications.sevirity import Severity

class Notification(BaseModel):
    id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    title: str
    message: str
    read_status = int
    severity: Severity
