from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive import Sensitive


class AccountIDPasswordLoginRequest(NormanBaseModel):
    account_id: str
    password: Sensitive[str]
