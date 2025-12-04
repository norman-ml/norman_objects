from typing import Optional

from norman_objects.shared.accounts.account import Account
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.security.sensitive import Sensitive


class LoginResponse(NormanBaseModel):
    """
    Response object returned after a successful authentication attempt.

    Includes the authenticated account and any issued access or identity
    tokens. Missing fields indicate partial or failed authentication flows.

    **Fields**

    - **account** (`Optional[Account]`)
      The authenticated account object.
      `None` if authentication failed or only token issuance was requested.

    - **access_token** (`Optional[Sensitive[str]]`)
      Bearer token granting access to protected API routes.
      Returned as `Sensitive` to avoid exposure.

    - **id_token** (`Optional[Sensitive[str]]`)
      Optional identity token (e.g., for session-based flows or UI clients).
    """
    account: Optional[Account] = None
    access_token: Optional[Sensitive[str]] = None
    id_token: Optional[Sensitive[str]] = None
