from norman_objects.norman_base_model import NormanBaseModel


class AccountAuthenticationMethods(NormanBaseModel):
    account_id: str
    api_keys_count: int
    passwords_count: int
    verified_emails_count: int

    def has_method_configured(self):
        return self.api_keys_count > 0 or self.passwords_count > 0 or self.verified_emails_count > 0
