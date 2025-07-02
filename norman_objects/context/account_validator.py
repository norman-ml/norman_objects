from contextlib import ContextDecorator

from norman_objects.context.context_tokens import NormanContext


class AccountValidator(ContextDecorator):
    def __init__(self, expected_account_id: str):
        self.expected_account_id = expected_account_id

    def __enter__(self):
        decoded_token = NormanContext.decoded_access_token.get(None)
        if decoded_token is None:
            raise ValueError("Cannot validate account without an access token.")

        decoded_token_raw = decoded_token.value()
        if not isinstance(decoded_token_raw, dict):
            raise ValueError("decoded_token_raw should be a dict.")

        token_account_id = decoded_token_raw.get("cognito:username")
        if token_account_id is None:
            raise ValueError("token_account_id has no property cognito:username.")

        if token_account_id != self.expected_account_id:
            raise PermissionError("Account ID mismatch. Access denied.")

        return self.expected_account_id

    def __exit__(self, exc_type, exc_val, exc_tb):
        # No return needed, default behavior propagates exceptions
        pass
