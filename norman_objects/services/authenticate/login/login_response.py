from typing import Optional

from norman_objects.shared.accounts.account import Account
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.security.sensitive import Sensitive


class LoginResponse(NormanBaseModel):
    account: Optional[Account] = None
    access_token: Optional[Sensitive[str]] = None
    id_token: Optional[Sensitive[str]] = None
