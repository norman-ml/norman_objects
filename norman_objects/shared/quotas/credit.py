from datetime import datetime, timezone, timedelta

from pydantic import BaseModel


class Credit(BaseModel):
    id: str = "0"
    quota_id: str
    start_date: datetime
    end_date: datetime
    billable: bool

    @classmethod
    def now(cls, quota_id: str, duration_seconds: int, billable: bool):
        now = datetime.now(timezone(timedelta(0)))
        return cls(
            quota_id=quota_id,
            start_date=now,
            end_date=now + timedelta(seconds=duration_seconds),
            billable=billable
        )
