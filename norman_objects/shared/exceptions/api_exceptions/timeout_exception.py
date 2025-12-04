from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class TimeoutException(NormanApiException):
    status_code: int = 504
    error_type: str = "timeout"
    suggestions: list[str] = [
        "Try again in a few moments",
        "Break the request into smaller operations",
        "Contact support if timeouts persist",
    ]
