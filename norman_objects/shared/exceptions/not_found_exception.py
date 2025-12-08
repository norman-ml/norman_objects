from typing import Optional

from norman_objects.shared.exceptions.norman_exception import NormanException


class NotFoundException(NormanException):
    status_code: int = 404
    error_type: str = "not_found"
    suggestions: list[str] = [
        "Verify the resource ID is correct",
        "Check if the resource has been deleted",
        "Ensure you have access to this resource"
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
            suggestions = NotFoundException.suggestions

        super().__init__(
            message=message,
            cause=cause,
            suggestions=suggestions,
            *args,
            **kwargs
        )

        self.status_code = NotFoundException.status_code
        self.error_type = NotFoundException.error_type
