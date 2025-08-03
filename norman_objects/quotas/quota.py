from datetime import datetime
from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.quotas.quota_type import QuotaType


class Quota(NormanBaseModel):
    id: str = "0"
    account_id: str
    type: QuotaType
    size: int
    start_date: datetime
    end_date: Optional[datetime] = None
