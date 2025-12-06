from typing import Optional

from norman_objects.shared.exceptions.internal_exceptions.infrastructure_exception import InfrastructureException


class DatabaseException(InfrastructureException):
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
            suggestions: Optional[list[str]] = None,
            cause: Optional[str] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = DatabaseException.suggestions

        super().__init__(
            message=message,
            error_type=DatabaseException.error_type,
            status_code=DatabaseException.status_code,
            suggestions=suggestions,
            cause=cause,
            *args,
            **kwargs
        )
