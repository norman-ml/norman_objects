import os
from typing import Callable

from norman_objects.context.context_tokens import NormanContext


class SecureFileContextManager:
    """
    Wraps `open()` in a context manager that enforces two security checks:

    1. The Cognito user ID embedded in the current access token must match
       `expected_account_id`.
    2. The Norman EFS file-path layout must include the same account ID in
       its fourth-from-last segment (…/<entity_type>/<phase>/<account_id>/<id>).

    By default the file is opened in binary write mode (“wb”), so it is
    created (or truncated) if it does not already exist.
    """

    def __init__(
        self,
        expected_account_id: str,
        path: str,
        open_file_context_manager: Callable = open,  # keep “open” static
        mode: str = "wb",                            # default write-binary
        *args,
        **kwargs,
    ):
        self.expected_account_id = expected_account_id
        self.path = path

        self.open_file_context_manager = open_file_context_manager
        self.method_args = args
        # ensure the chosen `mode` is forwarded to `open()`
        self.method_kwargs = {"mode": mode, **kwargs}

    # ------------------------------------------------------------------ #
    #                         context-manager API                        #
    # ------------------------------------------------------------------ #
    def __enter__(self):
        self.__security_checks()
        return self.open_file_context_manager(
            self.path, *self.method_args, **self.method_kwargs
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Propagate exceptions that occur inside the with-statement
        return False

    # ------------------------------------------------------------------ #
    #                           helper methods                           #
    # ------------------------------------------------------------------ #
    def __security_checks(self) -> None:
        """
        • Verifies that the account ID in the access token matches
          `expected_account_id`.
        • Verifies that the file path conforms to Norman’s five-segment
          layout and that the account-ID segment matches.
        """
        # --- token check ------------------------------------------------
        decoded_token = NormanContext.decoded_access_token.get(None)
        if decoded_token is None or not isinstance(decoded_token.value(), dict):
            raise ValueError("Cannot validate account without a proper access token")

        token_account_id = decoded_token.value().get("cognito:username")
        if token_account_id != self.expected_account_id:
            raise PermissionError("Account ID mismatch. Access denied.")

        # --- path structure check --------------------------------------
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
