from datetime import datetime, timezone, timedelta

from pydantic import BaseModel

from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class Credit(BaseModel):
    """
    Represents a credit unit applied to an account quota, such as a
    pre-purchased credit block, promotional credit, or billable usage token.

    **Fields**

    - **id** (`str`)
      Unique identifier for the credit record. Defaults to `"0"`.

    - **quota_id** (`str`)
      Identifier of the quota that this credit contributes to.

    - **start_date** (`datetime`)
      UTC timestamp indicating when the credit becomes active.

    - **end_date** (`datetime`)
      UTC timestamp indicating when the credit expires.

    - **billable** (`bool`)
      Whether this credit is billable (paid) or non-billable (e.g., bonus,
      trial credit, promotional allocation).
    """
    id: str = "0"
    quota_id: str
    start_date: NormalizedDateTime
    end_date: NormalizedDateTime
    billable: bool

    @classmethod
    def now(cls, quota_id: str, duration_seconds: int, billable: bool):
        now = datetime.now(timezone.utc)
        return cls(
            quota_id=quota_id,
            start_date=now,
            end_date=now + timedelta(seconds=duration_seconds),
            billable=billable
        )
