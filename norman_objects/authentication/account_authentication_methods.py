from norman_objects.norman_base_model import NormanBaseModel


class AccountAuthenticationMethods(NormanBaseModel):
    account_id: str
    api_key_count: int
    password_count: int
    verified_email_count: int

    def has_method_configured(self):
        return self.api_key_count > 0 or self.password_count > 0 or self.verified_email_count > 0
