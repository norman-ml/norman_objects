from norman_objects.norman_base_model import NormanBaseModel


class AccountAuthenticationMethods(NormanBaseModel):
    account_id: str
    passwords: int
    api_keys: int
    verified_emails: int
