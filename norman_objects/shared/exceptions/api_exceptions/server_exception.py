from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class ServerException(NormanApiException):
    status_code: int = 500
    error_type: str = "server"
    suggestions: list[str] = [
        "Try again in a few moments",
        "Contact support if the problem persists",
        "Check the service status page",
    ]
