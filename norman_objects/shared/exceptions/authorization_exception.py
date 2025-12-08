from typing import Optional

from norman_objects.shared.exceptions.norman_exception import NormanException


class AuthorizationException(NormanException):
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
            cause: Optional[str] = None,
            suggestions: Optional[list[str]] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = AuthorizationException.suggestions

        super().__init__(
            message=message,
            cause=cause,
            suggestions=suggestions,
            *args,
            **kwargs
        )

        self.status_code = AuthorizationException.status_code
        self.error_type = AuthorizationException.error_type
