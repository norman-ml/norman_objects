from datetime import datetime, timedelta, timezone
from typing import Optional

from pydantic import BaseModel, Field
from norman_objects.notifications.severity import Severity

from norman_objects.status_flags.status_flag_value import StatusFlagValue


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

    @classmethod
    def from_flag(cls, flag):
        if flag.flag_value == StatusFlagValue.Error:
            return cls(
                account_id=flag.account_id,
                entity_id=flag.entity_id,
                title="Error in Output Processing",
                message="Error encountered during model running. Please try again or contact support",
                read_status=0,
                severity=Severity.ERROR
            )

        elif flag.flag_value == StatusFlagValue.Finished:
            return cls(
                account_id=flag.account_id,
                entity_id=flag.entity_id,
                title="Output Processing Finished",
                message="Successfully finished model running",
                read_status=0,
                severity=Severity.INFO
            )
