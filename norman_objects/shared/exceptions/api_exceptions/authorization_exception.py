from typing import Optional

from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class AuthorizationException(NormanApiException):
    status_code: int = 403
    error_type: str = "authorization"
    suggestions: list[str] = [
        "Verify you have the required permissions",
        "Contact an administrator if you believe this is an error",
        "Check if your account has been restricted"
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
            suggestions = AuthorizationException.suggestions

        super().__init__(
            message=message,
            error_type=AuthorizationException.error_type,
            status_code=AuthorizationException.status_code,
            suggestions=suggestions,
            cause=cause,
            *args,
            **kwargs
        )
