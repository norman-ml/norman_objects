from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.quotas.quota_type import QuotaType


class QuotaUsage(NormanBaseModel):
    quota_id: str
    account_id: str
    start_date: NormalizedDateTime
    end_date: NormalizedDateTime
    type: QuotaType
    size: int
    used: int
    remaining: int
