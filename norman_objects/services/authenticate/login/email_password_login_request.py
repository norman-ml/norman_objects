from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.sensitive import Sensitive


class EmailPasswordLoginRequest(NormanBaseModel):
    email: str
    password: Sensitive[str]
