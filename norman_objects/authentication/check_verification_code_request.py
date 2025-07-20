from norman_objects.norman_base_model import NormanBaseModel


class CheckVerificationCodeRequest(NormanBaseModel):
    account_id: str
    code: str