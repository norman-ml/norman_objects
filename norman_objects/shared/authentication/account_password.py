from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class AccountPassword(NormanBaseModel):
    id: str = "0"
    account_id: str
    credential_hash_id: str
    created_at: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
