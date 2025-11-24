from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.security.sensitive import Sensitive


class RegisterAuthFactorRequest(NormanBaseModel):
    """
    Base request object for registering a new authentication factor
    (email, password, or other credential) to an existing account.

    **Fields**

    - **account_id** (`str`)
      Identifier of the account to which the authentication factor
      will be added.

    - **second_token** (`Optional[Sensitive[str]]`)
      Optional secondary verification token used in multi-step
      registration flows (e.g., linking a device, validating an email,
      or reinforcing a privileged operation).
      May be `None` if not required by the workflow.
    """
    account_id: str
    second_token: Optional[Sensitive[str]] = None
