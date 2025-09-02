from norman_objects.services.authenticate.register.register_auth_factor_request import RegisterAuthFactorRequest


class ResendEmailVerificationCodeRequest(RegisterAuthFactorRequest):
    email: str
