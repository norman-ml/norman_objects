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
            suggestions: Optional[list[str]] = None,
            cause: Optional[str] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = AuthenticationException.suggestions

        super().__init__(
            message=message,
            error_type=AuthenticationException.error_type,
            status_code=AuthenticationException.status_code,
            suggestions=suggestions,
            cause=cause,
            *args,
            **kwargs
        )
