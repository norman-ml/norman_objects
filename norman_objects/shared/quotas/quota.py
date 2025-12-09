from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.quotas.quota_type import QuotaType


class Quota(NormanBaseModel):
    """
    Represents a quota allocation assigned to an account, defining how much
    of a specific resource or credit type is available within a given time
    window.

    Quotas may represent base entitlements, accrued credits, pre-purchased
    capacity, or on-demand allocations.

    **Fields**

    - **id** (`str`)
      Unique identifier for the quota record. Defaults to `"0"`.

    - **account_id** (`str`)
      Identifier of the account receiving this quota.

    - **start_date** (`datetime`)
      UTC timestamp indicating when the quota becomes active.
      Defaults to the current time.

    - **end_date** (`datetime`)
      UTC timestamp indicating when the quota expires.
      Defaults to year 5000 (effectively "no expiration").

    - **type** (`QuotaType`)
      Category of quota allocation:
      - Base
      - Accrued
      - Pre_purchased
      - On_demand

    - **size** (`int`)
      Total amount of quota allocated.
    """
    id: str = "0"
    account_id: str
    start_date: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
    end_date: NormalizedDateTime = Field(default_factory=lambda: datetime(5000, 1, 1, 0, 0, 0, tzinfo=timezone.utc))
    type: QuotaType
    size: int


    @classmethod
    def base_quota(cls, account_id: str, size: int):
        return cls(
            account_id=account_id,
            type=QuotaType.Base,
            size=size
        )

    @classmethod
    def accrued_quota(cls, account_id: str, size: int):
        return cls(
            account_id=account_id,
            type=QuotaType.Accrued,
            size=size
        )

    @classmethod
    def pre_purchased_quota(cls, account_id: str, size: int):
        return cls(
            account_id=account_id,
            type=QuotaType.Pre_purchased,
            size=size
        )

    @classmethod
    def on_demand_quota(cls, account_id: str):
        return cls(
            account_id=account_id,
            type=QuotaType.On_demand,
            size=4294967295,  # Max possible quota size - https://dev.mysql.com/doc/refman/8.4/en/integer-types.html
        )
