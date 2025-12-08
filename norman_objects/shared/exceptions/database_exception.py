from typing import Optional

from norman_objects.shared.exceptions.norman_exception import NormanException


class DatabaseException(NormanException):
    status_code: int = 500
    error_type: str = "database"
    suggestions: list[str] = [
        "Try again in a few moments",
        "Contact support if the problem persists",
        "Check database connectivity"
    ]

    def __init__(
            self,
            message: str,
            cause: Optional[str] = None,
            suggestions: Optional[list[str]] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = DatabaseException.suggestions

        super().__init__(
            message=message,
            cause=cause,
            suggestions=suggestions,
            *args,
            **kwargs
        )

        self.status_code = DatabaseException.status_code
        self.error_type = DatabaseException.error_type
