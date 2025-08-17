from norman_objects.norman_base_model import NormanBaseModel


class AccountAuthenticationMethods(NormanBaseModel):
    account_id: str
    passwords: int
    api_keys: int
    verified_emails: int

    def has_any_method(self):
        return self.passwords > 0 or self.api_keys > 0 or self.verified_emails > 0
