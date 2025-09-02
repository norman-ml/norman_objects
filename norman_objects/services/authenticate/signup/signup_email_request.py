from norman_objects.norman_base_model import NormanBaseModel


class SignupEmailRequest(NormanBaseModel):
    name: str
    email: str
