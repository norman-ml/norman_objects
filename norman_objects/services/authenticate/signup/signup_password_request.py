from norman_objects.services.authenticate.signup.signup_request import SignupRequest
from norman_objects.shared.security.sensitive import Sensitive


class SignupPasswordRequest(SignupRequest):
    """
    Signup request for creating a new account using a password-based
    authentication flow.

    **Fields**

    - **device_id** (`Optional[str]`)
      Inherited from `SignupRequest`.

    - **name** (`str`)
      Chosen account name.

    - **password** (`Sensitive[str]`)
      User-provided password for the new account. Wrapped in `Sensitive`
      to ensure secure handling within logs and memory.
    """
    name: str
    password: Sensitive[str]
