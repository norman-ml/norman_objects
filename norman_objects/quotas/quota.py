from datetime import datetime, timezone, timedelta
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.quotas.quota_type import QuotaType
from pydantic import Field


class Quota(NormanBaseModel):
    id: str = "0"
    account_id: str
    start_date: datetime = Field(default_factory=lambda: datetime.now(UTC))
    end_date: datetime
    type: QuotaType
    size: int

    @classmethod
    def base_quota(cls, account_id: str, size: int = 20):
        now = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
        return cls(
            account_id=account_id,
            type=QuotaType.BASE,
            size=size,
            start_date=now,
            end_date=now + timedelta(days=31),
        )

    @classmethod
    def accrued_quota(cls, account_id: str, size: int = 10):
        now = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
        return cls(
            account_id=account_id,
            start_date=now,
            end_date=now + timedelta(days=31),
            type=QuotaType.ACCRUED,
            size=size
        )

    @classmethod
    def pre_purchased_quota(cls, account_id: str, size: int, duration_days: int = 365):
        now = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
        return cls(
            account_id=account_id,
            start_date=now,
            end_date=now + timedelta(days=duration_days),
            type=QuotaType.PRE_PURCHASED,
            size=size
        )

    @classmethod
    def on_demand_quota(cls, account_id: str):
        now = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
        return cls(
            account_id=account_id,
            start_date=now,
            end_date=now + timedelta(days=36500),  # 100 years
            type=QuotaType.ON_DEMAND,
            size=99999999,  # simulate "unlimited"
        )
