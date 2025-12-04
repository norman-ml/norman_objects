from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class AccountPassword(NormanBaseModel):
    """
    Represents a hashed password credential for an account.

    **Fields**

    - **id** (`str`)
      Unique identifier for the password record. Defaults to `"0"`.

    - **account_id** (`str`)
      Identifier of the account owning this password.

    - **credential_hash_id** (`str`)
      Identifier referencing the stored password hash.

    - **created_at** (`datetime`)
      UTC timestamp when the password was created.
    """
    id: str = "0"
    account_id: str
    credential_hash_id: str
    created_at: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
