import os
from typing import Callable

from norman_objects.context.context_tokens import NormanContext


class SecureFileContextManager:
    def __init__(self, account_id: str, path: str):
        self.account_id = account_id
        self.path = path

        self.file_handler = None

    def __enter__(self):
        self.security_checks()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def security_checks(self):
        decoded_token = NormanContext.decoded_access_token.get(None)
        if decoded_token is None or not isinstance(decoded_token.value(), dict):
            raise ValueError("Cannot validate account without a proper access token")

        token_account_id = decoded_token.value().get("cognito:username")
        if token_account_id != self.account_id:
            raise PermissionError("Account ID mismatch. Access denied.")

        segments = os.path.normpath(self.path).split(os.sep)
        try:
            (
                entity_type_segment,
                phase_segment,
                account_id_segment,
                entity_id_segment
            ) = segments[-4:]
        except ValueError:
            raise ValueError(f"File path {self.path} does not conform to expected 4-segment structure")

        if account_id_segment != self.account_id:
            raise PermissionError(f"Path account segment {account_id_segment} does not match expected account ID {self.account_id}")
