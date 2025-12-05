from typing import Optional

from norman_objects.shared.exceptions.api_exceptions.server_exception import ServerException
from norman_objects.shared.exceptions.norman_exception import NormanException


class NormanInternalException(NormanException):
    def __init__(
        self,
        message: str,
        original_exception: Optional[Exception] = None,
        cause: Optional[str] = None
    ):
        derived_cause = cause if cause is not None else (str(original_exception) if original_exception else None)
        super().__init__(
            message=message,
            cause=derived_cause,
        )
        self.original_exception = original_exception

    def to_api_exception(
        self,
        suggestions: Optional[list[str]] = None
    ):
        return ServerException(
            message=self.message,
            suggestions=suggestions,
            cause=self.cause
        )
