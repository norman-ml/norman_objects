from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.quotas.quota_type import QuotaType


class Quota(NormanBaseModel):
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
