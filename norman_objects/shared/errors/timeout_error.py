from norman_objects.shared.errors.norman_api_error import NormanApiError


class TimeoutError(NormanApiError):
    status_code: int = 504
    error_type: str = "timeout"
    suggestions: list[str] = [
        "Try again in a few moments",
        "Break the request into smaller operations",
        "Contact support if timeouts persist",
    ]
