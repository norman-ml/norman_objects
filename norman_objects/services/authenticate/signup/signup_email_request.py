from norman_objects.services.authenticate.signup.signup_request import SignupRequest


class SignupEmailRequest(SignupRequest):
    name: str
    email: str
