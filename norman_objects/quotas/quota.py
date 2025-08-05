from datetime import datetime, timedelta, UTC
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.quotas.quota_type import QuotaType
from pydantic import Field


class Quota(NormanBaseModel):
    id: str = "0"
    account_id: str
    type: QuotaType
    size: int
    start_date: datetime = Field(default_factory=lambda: datetime.now(UTC))
    end_date: datetime

    @classmethod
    def base_quota(cls, account_id: str, size: int = 20):
        now = datetime.now(UTC)
        return cls(
            account_id=account_id,
            type=QuotaType.BASE,
            size=size,
            start_date=now,
            end_date=now + timedelta(days=31),
        )

    @classmethod
    def accrued_quota(cls, account_id: str, size: int = 10):
        now = datetime.now(UTC)
        return cls(
            account_id=account_id,
            type=QuotaType.ACCRUED,
            size=size,
            start_date=now,
            end_date=now + timedelta(days=31),
        )

    @classmethod
    def pre_purchased_quota(cls, account_id: str, size: int, duration_days: int = 365):
        now = datetime.now(UTC)
        return cls(
            account_id=account_id,
            type=QuotaType.PRE_PURCHASED,
            size=size,
            start_date=now,
            end_date=now + timedelta(days=duration_days),
        )

    @classmethod
    def on_demand_quota(cls, account_id: str):
        now = datetime.now(UTC)
        return cls(
            account_id=account_id,
            type=QuotaType.ON_DEMAND,
            size=99999999,  # simulate "unlimited"
            start_date=now,
            end_date=now + timedelta(days=36500),  # 100 years
        )
