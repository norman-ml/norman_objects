from norman_objects.context.context_tokens import NormanContext


class SecureBucketContextManager:
    def __init__(self, account_id: str, key: str):
        self.account_id = account_id
        self.key = key

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

        segments = self.key.strip("/").split("/")
        account_id_segment = segments[0]

        if account_id_segment != self.account_id:
            raise PermissionError(f"Path account segment {account_id_segment} does not match expected account ID {self.account_id}")
