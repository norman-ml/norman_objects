from typing import Optional

from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class TimeoutException(NormanApiException):
    status_code: int = 504
    error_type: str = "timeout"
    suggestions: list[str] = [
        "Try again in a few moments",
        "Break the request into smaller operations",
        "Contact support if timeouts persist",
    ]

    def __init__(
            self,
            suggestions: Optional[list[str]] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = TimeoutException.suggestions

        super().__init__(
            error_type=TimeoutException.error_type,
            status_code=TimeoutException.status_code,
            suggestions=suggestions,
            *args,
            **kwargs
        )

