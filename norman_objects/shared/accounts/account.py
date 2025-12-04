from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class Account(NormanBaseModel):
    """
    Represents a user or tenant account within the Norman platform.

    Accounts serve as the root entity for identity, authentication,
    model ownership, quotas, notifications, and all platform resources.

    **Fields**

    - **id** (`str`)
      Unique identifier for the account. Defaults to `"0"`.

    - **creation_time** (`datetime`)
      UTC timestamp when the account was created.
      Defaults to the current time.

    - **name** (`str`)
      Human-readable name associated with the account.
    """
    id: str = "0"
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
    name: str
