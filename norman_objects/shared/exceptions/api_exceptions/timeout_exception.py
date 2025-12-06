from typing import Optional

from norman_objects.shared.exceptions.norman_exception import NormanException


class TimeoutException(NormanException):
    status_code: int = 504
    error_type: str = "timeout"
    suggestions: list[str] = [
        "Try again in a few moments",
        "Break the request into smaller operations",
        "Contact support if timeouts persist"
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
            suggestions = TimeoutException.suggestions

        super().__init__(
            message=message,
            error_type=TimeoutException.error_type,
            status_code=TimeoutException.status_code,
            suggestions=suggestions,
            cause=cause,
            *args,
            **kwargs
        )
