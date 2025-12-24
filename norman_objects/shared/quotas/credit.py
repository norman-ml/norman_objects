from datetime import datetime, timezone, timedelta

from pydantic import BaseModel

from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class Credit(BaseModel):
    id: str = "0"
    quota_id: str
    invocation_id: str
    start_date: NormalizedDateTime
    end_date: NormalizedDateTime
    billable: bool

    @classmethod
    def now(cls, quota_id: str, invocation_id: str, duration_seconds: int, billable: bool):
        now = datetime.now(timezone.utc)
        return cls(
            quota_id=quota_id,
            invocation_id=invocation_id,
            start_date=now,
            end_date=now + timedelta(seconds=duration_seconds),
            billable=billable
        )
