from typing import Optional

from norman_objects.shared.exceptions.internal_exceptions.infrastructure_exception import InfrastructureException


class CloudServiceException(InfrastructureException):
    status_code: int = 500
    error_type: str = "cloud_service"
    suggestions: list[str] = [
        "Try again in a few moments",
        "Contact support if the problem persists",
        "Check AWS service status"
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
            suggestions = CloudServiceException.suggestions

        super().__init__(
            message=message,
            error_type=CloudServiceException.error_type,
            status_code=CloudServiceException.status_code,
            suggestions=suggestions,
            cause=cause,
            *args,
            **kwargs
        )
