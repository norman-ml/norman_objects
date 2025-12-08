from typing import Optional

from norman_objects.shared.exceptions.norman_exception import NormanException


class AuthenticationException(NormanException):
    status_code: int = 401
    error_type: str = "authentication"
    suggestions: list[str] = [
        "Verify your credentials are correct",
        "Check if your session has expired",
        "Try logging in again"
    ]

    def __init__(
            self,
            message: str,
            cause: Optional[str] = None,
            suggestions: Optional[list[str]] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = AuthenticationException.suggestions

        super().__init__(
            message=message,
            cause=cause,
            suggestions=suggestions,
            *args,
            **kwargs
        )

        self.status_code = AuthenticationException.status_code
        self.error_type = AuthenticationException.error_type
