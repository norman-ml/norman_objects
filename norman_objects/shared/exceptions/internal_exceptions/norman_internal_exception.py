from datetime import datetime
from typing import Optional

from norman_objects.shared.exceptions.norman_exception import NormanException
from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException
from norman_objects.shared.exceptions.api_exceptions.server_exception import ServerException


class NormanInternalException(NormanException):

    def __init__(
        self,
        message: str,
        context: Optional[dict] = None,
        timestamp: Optional[datetime] = None,
        original_exception: Optional[Exception] = None
    ):
        NormanException.__init__(self, message=message, context=context, timestamp=timestamp)
        self.original_exception = original_exception

    def to_api_exception(
        self,
        default_message: Optional[str] = None,
        suggestions: Optional[list[str]] = None
    ) -> NormanApiException:
        message = default_message or self.message
        return ServerException(
            message=message,
            timestamp=self.timestamp,
            suggestions=suggestions
        )
