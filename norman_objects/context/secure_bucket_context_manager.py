from norman_objects.authorization.jwt_token import JwtToken
from norman_objects.context.norman_access_context import NormanAccessContext


class SecureBucketContextManager:
    def __init__(self, account_id: str, bucket_key: str):
        self.account_id = account_id
        self.bucket_key = bucket_key

    def __enter__(self):
        self.security_checks()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def security_checks(self):
        access_token = NormanAccessContext.get()
        if not isinstance(access_token, JwtToken):
            raise ValueError("Cannot validate account without a proper access token")

        token_account_id = access_token.payload.get("sub")
        if token_account_id != self.account_id:
            raise PermissionError("Account ID mismatch. Access denied.")

        segments = self.bucket_key.strip("/").split("/")
        account_id_segment = segments[0]

        if account_id_segment != self.account_id:
            raise PermissionError(f"Path account segment {account_id_segment} does not match expected account ID {self.account_id}")
