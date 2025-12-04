from typing import Optional

from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class ValidationException(NormanApiException):
    status_code: int = 400
    error_type: str = "validation"
    suggestions: list[str] = [
        "Check that all required fields are provided",
        "Verify the format of your input data",
        "Review the API documentation for parameter requirements"
    ]

    def __init__(
            self,
            suggestions: Optional[list[str]] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = ValidationException.suggestions

        super().__init__(
            error_type=ValidationException.error_type,
            status_code=ValidationException.status_code,
            suggestions=suggestions,
            *args,
            **kwargs
        )
