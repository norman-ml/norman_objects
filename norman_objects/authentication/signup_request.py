from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType


class SignupRequest(NormanBaseModel):
    name: str
    email: str
    password: SensitiveType(str)
