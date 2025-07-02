import asyncio
import os
from contextlib import ContextDecorator
from typing import IO, Any

from norman_objects.context.context_tokens import NormanContext


class SecureFileAccess(ContextDecorator):
    """
    Context manager that:
    1. Validates account ID in access token.
    2. Confirms the file path structure matches expected format.
    3. Verifies the account ID segment in the path.
    4. Optionally enforces file existence and size limits.
    5. Optionally returns a custom method instead of a file object.

    Required:
        - expected_account_id: str
        - path: str

    Optional kwargs:
        - must_exist: bool = True
        - max_size: int | None
        - mode: str = 'rb'
        - method: Callable to return instead of open()
        - method_args: tuple of positional args to pass to method
        - method_kwargs: dict of keyword args to pass to method
        - All other kwargs are passed to open()
    """

    def __init__(self, expected_account_id: str, path: str, **kwargs: Any):
        self.expected_account_id = expected_account_id
        self.path = path

        self.mode: str = kwargs.pop("mode", "rb")

        self.method = kwargs.pop("method", None)
        self.method_args = kwargs.pop("method_args", (self.path,))
        self.method_kwargs = kwargs.pop("method_kwargs", {})

        self.open_kwargs = kwargs  # any remaining kwargs go to open()
        self._file: IO | None = None

    def __enter__(self):
        # 1. Validate account identity
        decoded_token = NormanContext.decoded_access_token.get(None)
        if decoded_token is None or not isinstance(decoded_token.value(), dict):
            raise ValueError("Cannot validate account without a proper access token")

        token_account_id = decoded_token.value().get("cognito:username")
        if token_account_id != self.expected_account_id:
            raise PermissionError("Account ID mismatch. Access denied.")

        # 2. Validate path structure
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

        # 4. Return method result if provided
        if self.method is not None:
            return self.method(*self.method_args, **self.method_kwargs)

        # 5. Default: return open file handle
        self._file = open(self.path, self.mode, **self.open_kwargs)
        return self._file

    async def __aenter__(self):
        result = self.__enter__()
        if asyncio.iscoroutine(result):
            return await result
        return result

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.close()
        return False

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return self.__exit__(exc_type, exc_val, exc_tb)
