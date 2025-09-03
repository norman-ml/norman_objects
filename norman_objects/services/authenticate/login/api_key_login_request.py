from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.security.sensitive import Sensitive


class ApiKeyLoginRequest(NormanBaseModel):
    account_id: str
    api_key: Sensitive[str]
