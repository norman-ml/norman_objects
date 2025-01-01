from datetime import datetime, timedelta, timezone
from typing import Optional

from pydantic import BaseModel, Field
from norman_objects.notifications.severity import Severity

from norman_objects.status_flags.status_flag_value import StatusFlagValue

from norman_objects.status_flags.status_flag import StatusFlag


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
    def from_flag(cls, status_flag: StatusFlag): # TODO: think about mechanisem for other StatusFlagValue
        if status_flag.flag_value == StatusFlagValue.Error:
            return cls(
                account_id=status_flag.account_id,
                entity_id=status_flag.entity_id,
                title="Error in Output Processing",
                message="Error encountered during model running. Please try again or contact support",
                read_status=0,
                severity=Severity.Error
            )

        elif status_flag.flag_value == StatusFlagValue.Finished:
            return cls(
                account_id=status_flag.account_id,
                entity_id=status_flag.entity_id,
                title="Output Processing Finished",
                message="Successfully finished model running",
                read_status=0,
                severity=Severity.Info
            )
