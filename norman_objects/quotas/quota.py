from datetime import datetime, timezone, timedelta

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.quotas.quota_type import QuotaType
from pydantic import Field


class Quota(NormanBaseModel):
    id: str = "0"
    account_id: str
    start_date: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    end_date: datetime = Field(    default_factory=lambda: datetime(5000, 1, 1, 0, 0, 0, tzinfo=timezone(timedelta(0))))
    type: QuotaType
    size: int

    @classmethod
    def base_quota(cls, account_id: str, size: int):
        now = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
        return cls(
            account_id=account_id,
            type=QuotaType.BASE,
            size=size,
            start_date=now
        )

    @classmethod
    def accrued_quota(cls, account_id: str, size: int):
        now = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
        return cls(
            account_id=account_id,
            start_date=now,
            type=QuotaType.ACCRUED,
            size=size
        )

    @classmethod
    def pre_purchased_quota(cls, account_id: str, size: int):
        now = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
        return cls(
            account_id=account_id,
            start_date=now,
            type=QuotaType.PRE_PURCHASED,
            size=size
        )

    @classmethod
    def on_demand_quota(cls, account_id: str):
        now = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
        return cls(
            account_id=account_id,
            start_date=now,
            type=QuotaType.ON_DEMAND,
            size=4294967295,  # Max possible quota size - "https://dev.mysql.com/doc/refman/8.4/en/integer-types.html"
        )
