from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from norman_objects.notifications.severity import Severity

class Notification(BaseModel):
    id: Optional[str] = None
    creation_time: Optional[datetime] = None
    title: str
    message: str
    read_status: int = 0
    severity: Severity
