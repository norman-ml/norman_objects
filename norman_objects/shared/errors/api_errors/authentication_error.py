from norman_objects.shared.errors.api_errors.norman_api_error import NormanApiError


class AuthenticationError(NormanApiError):
    status_code: int = 401
    error_type: str = "authentication"
    suggestions: list[str] = [
        "Verify your credentials are correct",
        "Check if your session has expired",
        "Try logging in again",
    ]
