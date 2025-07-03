import os
from typing import Callable

from norman_objects.context.context_tokens import NormanContext


class SecureFileContextManager:
    def __init__(self, account_id: str, path: str, file_method: Callable = None, *args, **kwargs):
        self.account_id = account_id
        self.path = path

        self.file_method = file_method
        self.file_method_args = args
        self.file_method_kwargs = kwargs

        self.file_handler = None

    def __enter__(self):
        self.security_checks()

        if self.file_method is not None:
            self.file_handler = self.file_method(self.path, *self.file_method_args, **self.file_method_kwargs)

        return self.file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):      # △ protocol signature
        if self.file_handler and callable(getattr(self.file_handler, "close", None)):  # △
            try:
                self.file_handler.close()
            except Exception:
                pass
        return False

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
                _mountpoint,
                entity_type_segment,
                phase_segment,
                account_id_segment,
                entity_id_segment,
            ) = segments[-5:]
        except ValueError:
            raise ValueError(
                f"File path {self.path!r} does not conform to expected 5-segment structure"
            )

        if account_id_segment != self.account_id:
            raise PermissionError(
                f"Path account segment {account_id_segment!r} does not match "
                f"expected account ID {self.account_id!r}"
            )