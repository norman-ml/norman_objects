from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class AccountApiKey(NormanBaseModel):
    """
    Represents an API key associated with an account, stored in a secure
    hashed form. Each key maps to a credential hash entry and includes
    creation timestamp metadata.

    **Fields**

    - **id** (`str`)
      Unique identifier for the API key record. Defaults to `"0"`.

    - **account_id** (`str`)
      Identifier of the account that owns this API key.

    - **credential_hash_id** (`str`)
      Identifier referencing the stored hashed credential.

    - **created_at** (`datetime`)
      UTC timestamp when the API key was created. Defaults to now.
    """
    id: str = "0"
    account_id: str
    credential_hash_id: str
    created_at: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
