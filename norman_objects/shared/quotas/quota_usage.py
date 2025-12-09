from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.quotas.quota_type import QuotaType


class QuotaUsage(NormanBaseModel):
    """
    Represents a usage breakdown for a specific quota allocation within a
    defined date range.

    Tracks how much of the quota has been consumed, how much remains, and
    the exact quota type and lifecycle window.

    **Fields**

    - **quota_id** (`str`)
      Identifier of the quota record being measured.

    - **account_id** (`str`)
      Account associated with this usage entry.

    - **start_date** (`datetime`)
      UTC timestamp marking the beginning of the usage window.

    - **end_date** (`datetime`)
      UTC timestamp marking the end of the usage window.

    - **type** (`QuotaType`)
      Quota category associated with this usage (Base, Accrued, etc.).

    - **size** (`int`)
      Total available quota for this interval.

    - **used** (`int`)
      Amount of quota consumed within the interval.

    - **remaining** (`int`)
      Amount of quota still available.
      Typically computed as `size - used`.
    """
    quota_id: str
    account_id: str
    start_date: NormalizedDateTime
    end_date: NormalizedDateTime
    type: QuotaType
    size: int
    used: int
    remaining: int
