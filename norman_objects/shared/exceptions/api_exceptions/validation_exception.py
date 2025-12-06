from typing import Optional

from norman_objects.shared.exceptions.norman_exception import NormanException


class ValidationException(NormanException):
    status_code: int = 400
    error_type: str = "validation"
    suggestions: list[str] = [
        "Check that all required fields are provided",
        "Verify the format of your input data",
        "Review the API documentation for parameter requirements"
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
            suggestions = ValidationException.suggestions

        super().__init__(
            message=message,
            error_type=ValidationException.error_type,
            status_code=ValidationException.status_code,
            suggestions=suggestions,
            cause=cause,
            *args,
            **kwargs
        )
