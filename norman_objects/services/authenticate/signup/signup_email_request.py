from norman_objects.services.authenticate.signup.signup_request import SignupRequest


class SignupEmailRequest(SignupRequest):
    """
    Signup request for creating a new account using an email address
    and account name.

    **Fields**

    - **device_id** (`Optional[str]`)
      Inherited from `SignupRequest`.

    - **name** (`str`)
      Human-readable account name chosen during signup.

    - **email** (`str`)
      Email address used for account creation and verification.
    """
    name: str
    email: str
