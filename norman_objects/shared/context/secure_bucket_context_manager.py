from norman_objects.shared.authorization.jwt_token import JwtToken
from norman_objects.shared.context.norman_access_context import NormanAccessContext


class SecureBucketContextManager:
    def __init__(self, account_id: str, bucket_key: str):
        self.account_id = account_id
        self.bucket_key = bucket_key

    def __enter__(self):
        self.security_checks()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def security_checks(self):
        if ".." in self.bucket_key:
            raise ValueError("Jailbreak attempt detected - backtracking in bucket key")

        access_token = NormanAccessContext.get()
        if not isinstance(access_token, JwtToken):
            raise ValueError("Cannot validate account without a proper access token")

        token_account_id = access_token.payload.get("sub")
        if token_account_id != self.account_id:
            raise PermissionError("Account ID mismatch. Access denied.")

        segments = self.bucket_key.strip("/").split("/")
        if self.account_id not in segments:
            raise PermissionError(f"Bucket key {self.bucket_key} does not contain expected account ID {self.account_id}")
