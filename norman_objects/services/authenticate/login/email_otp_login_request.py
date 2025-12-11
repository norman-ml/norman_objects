from norman_objects.norman_base_model import NormanBaseModel


class EmailOtpLoginRequest(NormanBaseModel):
    email: str