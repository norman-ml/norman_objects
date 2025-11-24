from norman_objects.shared.security.sensitive import Sensitive
from norman_objects.services.authenticate.register.register_auth_factor_request import RegisterAuthFactorRequest


class RegisterPasswordRequest(RegisterAuthFactorRequest):
    """
    Request object for registering a password as an authentication factor
    for an account.

    **Fields**

    - **account_id** (`str`)
      Inherited from `RegisterAuthFactorRequest`.

    - **second_token** (`Optional[Sensitive[str]]`)
      Inherited from `RegisterAuthFactorRequest`.

    - **password** (`Sensitive[str]`)
      Password to be securely registered. Wrapped in `Sensitive` to prevent
      exposure in logs or traces.
    """
    password: Sensitive[str]
