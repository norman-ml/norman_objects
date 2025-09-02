from norman_objects.shared.sensitive import Sensitive
from norman_objects.services.authenticate.register.register_auth_factor_request import RegisterAuthFactorRequest


class RegisterPasswordRequest(RegisterAuthFactorRequest):
    password: Sensitive[str]
