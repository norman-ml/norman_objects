from norman_objects.shared.errors.api_errors.norman_api_error import NormanApiError


class ServerError(NormanApiError):
    status_code: int = 500
    error_type: str = "server_error"
    suggestions: list[str] = [
        "Try again in a few moments",
        "Contact support if the problem persists",
        "Check the service status page",
    ]
