from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.sensitive import Sensitive


class NamePasswordLoginRequest(NormanBaseModel):
    name: str
    password: Sensitive[str]
