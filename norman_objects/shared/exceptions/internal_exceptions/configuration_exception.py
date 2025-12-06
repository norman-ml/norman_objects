from typing import Optional

from norman_objects.shared.exceptions.internal_exceptions.infrastructure_exception import InfrastructureException


class ConfigurationException(InfrastructureException):
    status_code: int = 500
    error_type: str = "configuration"
    suggestions: list[str] = [
        "Try again in a few moments",
        "Contact support if the problem persists",
        "Check configuration service status"
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
            suggestions = ConfigurationException.suggestions

        super().__init__(
            message=message,
            error_type=ConfigurationException.error_type,
            status_code=ConfigurationException.status_code,
            suggestions=suggestions,
            cause=cause,
            *args,
            **kwargs
        )
