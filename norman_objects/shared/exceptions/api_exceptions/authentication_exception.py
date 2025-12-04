from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class AuthenticationException(NormanApiException):
    status_code: int = 401
    error_type: str = "authentication"
    suggestions: list[str] = [
        "Verify your credentials are correct",
        "Check if your session has expired",
        "Try logging in again",
    ]
