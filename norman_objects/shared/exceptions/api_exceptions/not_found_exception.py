from typing import Optional

from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class NotFoundException(NormanApiException):
    status_code: int = 404
    error_type: str = "not_found"
    suggestions: list[str] = [
        "Verify the resource ID is correct",
        "Check if the resource has been deleted",
        "Ensure you have access to this resource",
    ]

    def __init__(
            self,
            suggestions: Optional[list[str]] = None,
            *args,
            **kwargs
    ):
        if suggestions is None:
            suggestions = NotFoundException.suggestions

        super().__init__(
            error_type=NotFoundException.error_type,
            status_code=NotFoundException.status_code,
            suggestions=suggestions,
            *args,
            **kwargs
        )
