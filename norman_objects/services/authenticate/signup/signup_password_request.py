from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.security.sensitive import Sensitive


class SignupPasswordRequest(NormanBaseModel):
    name: str
    password: Sensitive[str]
