from datetime import datetime, timezone, timedelta
from typing import Optional
from pydantic import BaseModel

from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class Credit(BaseModel):
    id: str = "0"
    quota_id: str
    model_invocation_id: Optional[str] = None
    start_date: NormalizedDateTime
    end_date: NormalizedDateTime
    billable: bool

    @classmethod
    def now(cls, quota_id: str, duration_seconds: int, billable: bool, model_invocation_id: Optional[str] = None):
        now = datetime.now(timezone.utc)
        return cls(
            quota_id=quota_id,
            model_invocation_id=model_invocation_id,
            start_date=now,
            end_date=now + timedelta(seconds=duration_seconds),
            billable=billable
        )
