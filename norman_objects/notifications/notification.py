from datetime import datetime, timedelta, timezone
from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from pydantic import Field

class Notification(NormanBaseModel):
    id: str
    account_id: str
    entity_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    title: str
    message: str
    read_status: int
    severity: Severity
    notification_type: NotificationType



