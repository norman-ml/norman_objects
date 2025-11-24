from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel


class SignupRequest(NormanBaseModel):
    """
    Base request object for initiating a signup flow.

    Signup requests may include device metadata or be extended with
    email, password, or API-key-based registration details.

    **Fields**

    - **device_id** (`Optional[str]`)
      Optional device identifier used for device-bound authentication,
      security tracking, or account attribution.
      May be `None` if no device information is provided.
    """
    device_id: Optional[str] = None
