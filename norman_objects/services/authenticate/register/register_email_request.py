from norman_objects.services.authenticate.register.register_auth_factor_request import RegisterAuthFactorRequest


class RegisterEmailRequest(RegisterAuthFactorRequest):
    """
    Request object for registering a new email address as an authentication
    factor for an account.

    Inherits the core registration fields and adds the email to be linked.

    **Fields**

    - **account_id** (`str`)
      Inherited from `RegisterAuthFactorRequest`.

    - **second_token** (`Optional[Sensitive[str]]`)
      Inherited from `RegisterAuthFactorRequest`.

    - **email** (`str`)
      Email address to register and verify for this account.
    """
    email: str
