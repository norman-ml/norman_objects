from contextlib import ContextDecorator

from norman_objects.context.context_tokens import NormanContext


class AccountValidator(ContextDecorator):
    def __init__(self, expected_account_id: str):
        self.expected_account_id = expected_account_id

    def __enter__(self):
        decoded_token = NormanContext.decoded_access_token.get(None)
        token_account_id = decoded_token.value().get("cognito:username")

        if token_account_id != self.expected_account_id:
            raise PermissionError("Account ID mismatch. Access denied.")

        return self.expected_account_id

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
