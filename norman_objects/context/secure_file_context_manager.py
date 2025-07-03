import os
from typing import Callable

from norman_objects.context.context_tokens import NormanContext


class SecureFileContextManager:
    def __init__(self, expected_account_id:str , path: str, open_file_context_manager: Callable = None, *args, **kwargs):
        self.expected_account_id = expected_account_id
        self.path = path

        if open_file_context_manager is None:
            open_file_context_manager = open

        self.open_file_context_manager = open_file_context_manager
        self.method_args = args
        self.method_kwargs = kwargs

    def __enter__(self):
        self.__security_checks()
        # keep a reference so we can close it later
        self._handle = self.open_file_context_manager(
            self.path, *self.method_args, **self.method_kwargs
        )
        return self._handle


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        exc_type, exc_val, exc_tb are required by the CM protocol.
        We close the file if it was opened and propagate any exception
        that occurred inside the with-block (return False).
        """
        if getattr(self, "_handle", None):
            try:
                self._handle.close()
            except Exception:
                # log or ignore – but don’t hide the original error
                pass
        return False    # re-raise exceptions from the with-block

    def __security_checks(self):
        decoded_token = NormanContext.decoded_access_token.get(None)
        if decoded_token is None or not isinstance(decoded_token.value(), dict):
            raise ValueError("Cannot validate account without a proper access token")

        token_account_id = decoded_token.value().get("cognito:username")
        if token_account_id != self.expected_account_id:
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

        if account_id_segment != self.expected_account_id:
            raise PermissionError(
                f"Path account segment {account_id_segment!r} does not match "
                f"expected account ID {self.expected_account_id!r}"
            )