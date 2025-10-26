from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.accounts.account import Account


class SignupKeyResponse(NormanBaseModel):
    account: Account
    api_key: str
