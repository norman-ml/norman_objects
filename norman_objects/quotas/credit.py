from pydantic import BaseModel
from datetime import datetime, timedelta, UTC

class Credit(BaseModel):
    id: str = "0"
    quota_id: str
    start_date: datetime
    end_date: datetime
    billable: bool = False

    @classmethod
    def now(cls, quota_id: str, duration_seconds: int, billable: bool):
        now = datetime.now(UTC)
        return cls(
            id="0",
            quota_id=quota_id,
            start_date=now,
            end_date=now + timedelta(seconds=duration_seconds),
            billable=billable
        )
