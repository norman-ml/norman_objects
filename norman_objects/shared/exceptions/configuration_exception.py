from typing import Optional

from norman_objects.shared.exceptions.norman_exception import NormanException


class ConfigurationException(NormanException):
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
            cause: Optional[str] = None,
            suggestions: Optional[list[str]] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = ConfigurationException.suggestions

        super().__init__(
            message=message,
            cause=cause,
            suggestions=suggestions,
            *args,
            **kwargs
        )

        self.status_code = ConfigurationException.status_code
        self.error_type = ConfigurationException.error_type
