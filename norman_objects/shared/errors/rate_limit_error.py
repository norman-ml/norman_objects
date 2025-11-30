from norman_objects.shared.errors.norman_api_error import NormanApiError


class RateLimitError(NormanApiError):
    status_code: int = 429
    error_type: str = "rate_limit"
    suggestions: list[str] = [
        "Wait a moment before trying again",
        "Check your quota limits",
        "Contact support to increase your limits",
    ]
