from norman_objects.norman_base_model import NormanBaseModel


class StoreVerificationCodeRequest(NormanBaseModel):
    account_id: str
    email: str
    code: str
    expiration_seconds: int = 300  # default 5 minutes