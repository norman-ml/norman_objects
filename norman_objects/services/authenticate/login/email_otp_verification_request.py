from norman_objects.norman_base_model import NormanBaseModel


class  EmailOTPVerificationRequest(NormanBaseModel):
    email: str
    code: str