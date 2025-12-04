from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class RateLimitException(NormanApiException):
    status_code: int = 429
    error_type: str = "rate_limit"
    suggestions: list[str] = [
        "Wait a moment before trying again",
        "Check your quota limits",
        "Contact support to increase your limits",
    ]
