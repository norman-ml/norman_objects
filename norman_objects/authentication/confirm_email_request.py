from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType


class ConfirmEmailRequest(NormanBaseModel):
    account_id: str
    email: str
    confirmation_code: SensitiveType(str)
