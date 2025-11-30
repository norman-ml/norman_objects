from norman_objects.shared.errors.norman_api_error import NormanApiError


class AuthorizationError(NormanApiError):
    status_code: int = 403
    error_type: str = "authorization"
    suggestions: list[str] = [
        "Verify you have the required permissions",
        "Contact an administrator if you believe this is an error",
        "Check if your account has been restricted",
    ]
