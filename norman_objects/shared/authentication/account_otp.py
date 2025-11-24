from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class AccountOTP(NormanBaseModel):
    """
    Represents a One-Time Password (OTP) credential for account verification
    or login flows.

    **Fields**

    - **id** (`str`)
      Unique identifier for the OTP entry. Defaults to `"0"`.

    - **account_id** (`str`)
      Identifier of the account associated with the OTP.

    - **credential_hash_id** (`str`)
      Identifier referencing the hashed OTP credential.

    - **created_at** (`datetime`)
      UTC timestamp when the OTP was generated.

    - **verified** (`bool`)
      Whether the OTP was successfully used. Defaults to `False`.
    """
    id: str = "0"
    account_id: str
    credential_hash_id: str
    created_at: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
    verified: bool = False
