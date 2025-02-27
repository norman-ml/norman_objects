from datetime import datetime, timedelta, timezone
from typing import Optional

from norman_objects.norman_base_model.norman_bose_model import NormanBaseModel
from norman_objects.notifications.severity import Severity
from pydantic import Field


class InvocationNotification(NormanBaseModel):
    id: str
    account_id: str
    entity_id: str
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    model_name: Optional[str] = None
    title: str
    message: str
    read_status: int
    severity: Severity
