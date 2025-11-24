from norman_objects.norman_base_model import NormanBaseModel


class AccountAuthenticationMethods(NormanBaseModel):
    """
    Aggregated summary of available authentication methods for an account.

    **Fields**

    - **account_id** (`str`)
      Identifier of the account.

    - **api_key_count** (`int`)
      Number of active API keys associated with the account.

    - **password_count** (`int`)
      Number of password-based login credentials.

    - **verified_email_count** (`int`)
      Number of email addresses verified for authentication or recovery.
    """
    account_id: str
    api_key_count: int
    password_count: int
    verified_email_count: int

    def has_method_configured(self):
        return self.api_key_count > 0 or self.password_count > 0 or self.verified_email_count > 0
