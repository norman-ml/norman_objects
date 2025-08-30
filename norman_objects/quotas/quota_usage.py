from datetime import datetime

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.quotas.quota_type import QuotaType


class QuotaUsage(NormanBaseModel):
    quota_id: str
    account_id: str
    start_date: datetime
    end_date: datetime
    type: QuotaType
    size: int
    used: int
    remaining: int
