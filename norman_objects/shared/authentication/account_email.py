from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class AccountEmail(NormanBaseModel):
    """
    Represents an email credential associated with an account, including
    verification state and optional OTP linkage.

    **Fields**

    - **id** (`str`)
      Unique email record identifier. Defaults to `"0"`.

    - **account_id** (`str`)
      Identifier of the account that owns this email.

    - **account_otp_id** (`str`)
      Identifier of the OTP record linked to this email, if any.
      Defaults to `"0"`.

    - **created_at** (`datetime`)
      Timestamp (UTC) when this email record was created.

    - **email** (`str`)
      Email address.

    - **verified** (`bool`)
      Whether the email address has been verified. Defaults to `False`.
    """
    id: str = "0"
    account_id: str
    account_otp_id: str = "0"
    created_at: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
    email: str
    verified: bool = False
