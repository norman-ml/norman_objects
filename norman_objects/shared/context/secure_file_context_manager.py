import os

from norman_objects.shared.authorization.jwt_token import JwtToken
from norman_objects.shared.context.norman_access_context import NormanAccessContext


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
        if ".." in self.path:
            raise ValueError("Jailbreak attempt detected - backtracking in file path")

        access_token = NormanAccessContext.get()
        if not isinstance(access_token, JwtToken):
            raise ValueError("Cannot validate account without a proper access token")

        token_account_id = access_token.payload.get("sub")
        if token_account_id != self.account_id:
            raise PermissionError("Account ID mismatch. Access denied.")

        segments = os.path.normpath(self.path).split(os.sep)
        try:
            (
                mountpoint,
                entity_type_segment,
                phase_segment,
                state_segment,
                account_id_segment
            ) = segments[:5]
        except ValueError:
            raise ValueError(f"File path {self.path} does not start with the expected 5-segment structure")

        if account_id_segment != self.account_id:
            raise PermissionError(f"Path account segment {account_id_segment} does not match expected account ID {self.account_id}")
