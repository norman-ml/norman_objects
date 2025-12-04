from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class AccountDevice(NormanBaseModel):
    """
    Represents a device associated with an account, typically used for
    security, session management, or tracking login history.

    **Fields**

    - **id** (`str`)
      Unique identifier for the device record. Defaults to `"0"`.

    - **account_id** (`str`)
      Identifier of the account that owns this device.

    - **device_id** (`str`)
      Platform or client-specific identifier for the device
      (e.g., browser fingerprint, hardware ID, mobile device token).

    - **created_at** (`datetime`)
      UTC timestamp when this device record was created.
      Defaults to the current time.
    """
    id: str = "0"
    account_id: str
    device_id: str
    created_at: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
