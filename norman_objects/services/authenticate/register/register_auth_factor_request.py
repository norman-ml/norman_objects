from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.sensitive import Sensitive


class RegisterAuthFactorRequest(NormanBaseModel):
    account_id: str
    second_token: Optional[Sensitive[str]] = None
