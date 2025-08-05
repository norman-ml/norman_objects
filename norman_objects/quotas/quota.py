from datetime import datetime, timedelta
from typing import Optional

from pydantic import root_validator
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.quotas.quota_type import QuotaType


class Quota(NormanBaseModel):
    id: str = "0"
    account_id: str
    type: QuotaType
    size: int
    start_date: datetime
    end_date: datetime = None

    # @root_validator(pre=True) ensures this logic runs before field validation.
    @root_validator(pre=True)
    def set_default_end_date(cls, values):
        start = values.get("start_date")
        end = values.get("end_date")
        if start is not None and end is None:
            values["end_date"] = start + timedelta(days=31)  # ~1 month
        return values
