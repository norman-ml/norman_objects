from datetime import datetime, timezone
from pydantic import Field
from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.notifications.severity import Severity


class Notification(NormanBaseModel):
    id: str
    account_id: str
    entity_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    model_name: Optional[str] = None
    title: str
    message: str
    read_status: int
    severity: Severity
