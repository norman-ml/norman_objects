from norman_objects.services.authenticate.signup.signup_request import SignupRequest
from norman_objects.shared.security.sensitive import Sensitive


class SignupPasswordRequest(SignupRequest):
    name: str
    password: Sensitive[str]
