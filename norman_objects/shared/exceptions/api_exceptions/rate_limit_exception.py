from typing import Optional

from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class RateLimitException(NormanApiException):
    status_code: int = 429
    error_type: str = "rate_limit"
    suggestions: list[str] = [
        "Wait a moment before trying again",
        "Check your quota limits",
        "Contact support to increase your limits",
    ]

    def __init__(
            self,
            suggestions: Optional[list[str]] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = RateLimitException.suggestions

        super().__init__(
            error_type=RateLimitException.error_type,
            status_code=RateLimitException.status_code,
            suggestions=suggestions,
            *args,
            **kwargs
        )
