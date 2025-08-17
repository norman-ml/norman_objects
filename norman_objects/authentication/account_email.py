from datetime import datetime, timezone

from norman_objects.norman_base_model import NormanBaseModel
from pydantic import EmailStr
from pydantic import Field


class AccountEmail(NormanBaseModel):
    id: str = "0"
    account_id: str
    credential_hash_id: str = "0"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    email: EmailStr
    verified: bool = False
