from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.security.sensitive import Sensitive


class EmailPasswordLoginRequest(NormanBaseModel):
    """
    Authentication request using an email address and password.

    This is the standard user-facing login flow.

    **Fields**

    - **email** (`str`)
      Email address associated with the account.

    - **password** (`Sensitive[str]`)
      User password, wrapped in `Sensitive` for secure handling.
    """
    email: str
    password: Sensitive[str]
