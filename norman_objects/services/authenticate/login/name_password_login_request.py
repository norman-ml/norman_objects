from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.security.sensitive import Sensitive


class NamePasswordLoginRequest(NormanBaseModel):
    """
    Authentication request using an account name (username) and password.

    This request supports username-based login flows, especially useful for
    systems where account names are unique identifiers.

    **Fields**

    - **name** (`str`)
      Username or human-readable account name.

    - **password** (`Sensitive[str]`)
      User password stored in a secure container.
    """
    name: str
    password: Sensitive[str]
