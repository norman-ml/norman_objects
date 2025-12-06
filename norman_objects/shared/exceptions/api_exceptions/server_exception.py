from typing import Optional

from norman_objects.shared.exceptions.norman_exception import NormanException


class ServerException(NormanException):
    status_code: int = 500
    error_type: str = "server"
    suggestions: list[str] = [
        "Try again in a few moments",
        "Contact support if the problem persists",
        "Check the service status page"
    ]

    def __init__(
            self,
            message: str,
            suggestions: Optional[list[str]] = None,
            cause: Optional[str] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = ServerException.suggestions

        super().__init__(
            message=message,
            error_type=ServerException.error_type,
            status_code=ServerException.status_code,
            suggestions=suggestions,
            cause=cause,
            *args,
            **kwargs
        )
