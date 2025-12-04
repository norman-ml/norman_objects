from typing import Optional

from norman_objects.shared.exceptions.api_exceptions.server_exception import ServerException
from norman_objects.shared.exceptions.norman_exception import NormanException


class NormanInternalException(NormanException):
    def __init__(
        self,
        message: str,
        original_exception: Optional[Exception] = None
    ):
        super().__init__(message=message)
        self.original_exception = original_exception

    def to_api_exception(
        self,
        suggestions: list[str]
    ):
        return ServerException(
            message=self.message,
            suggestions=suggestions
        )
