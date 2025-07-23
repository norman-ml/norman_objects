from norman_objects.sensitive.sensitive_type import SensitiveType
from pydantic import BaseModel


class SetPasswordRequest(BaseModel):
    account_id: str
    email: str
    password: SensitiveType(str)
