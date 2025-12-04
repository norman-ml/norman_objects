from typing import Optional

from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class AuthenticationException(NormanApiException):
    status_code: int = 401
    error_type: str = "authentication"
    suggestions: list[str] = [
        "Verify your credentials are correct",
        "Check if your session has expired",
        "Try logging in again"
    ]

    def __init__(
            self,
            suggestions: Optional[list[str]] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = AuthenticationException.suggestions

        super().__init__(
            error_type=AuthenticationException.error_type,
            status_code=AuthenticationException.status_code,
            suggestions=suggestions,
            *args,
            **kwargs
        )
