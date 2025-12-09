from norman_objects.services.authenticate.signup.signup_request import SignupRequest


class SignupKeyRequest(SignupRequest):
    """
    Signup request for creating an account that will authenticate
    strictly via API key.

    This flow is typically used for machine-to-machine or programmatic
    access scenarios.

    **Fields**

    - **device_id** (`Optional[str]`)
      Inherited from `SignupRequest`.

    - **name** (`str`)
      Display name or identifier for the new account.
    """
    name: str
