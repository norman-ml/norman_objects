from norman_objects.services.authenticate.register.register_auth_factor_request import RegisterAuthFactorRequest


class ResendEmailVerificationCodeRequest(RegisterAuthFactorRequest):
    """
    Request object for resending an email verification code to a user who
    is in the process of registering an email authentication factor.

    **Fields**

    - **account_id** (`str`)
      Inherited from `RegisterAuthFactorRequest`.

    - **second_token** (`Optional[Sensitive[str]]`)
      Inherited from `RegisterAuthFactorRequest`.

    - **email** (`str`)
      Email address to which the verification code should be re-sent.
    """
    email: str
