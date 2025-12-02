from norman_objects.shared.errors.api_errors.norman_api_error import NormanApiError


class ValidationError(NormanApiError):
    status_code: int = 400
    error_type: str = "validation"
    suggestions: list[str] = [
        "Check that all required fields are provided",
        "Verify the format of your input data",
        "Review the API documentation for parameter requirements",
    ]
