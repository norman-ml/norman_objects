from datetime import datetime, UTC
from typing import Optional

from norman_objects.shared.errors.norman_error import NormanError


class NormanInternalException(NormanError):

    def __init__(
        self,
        message: str,
        details: Optional[dict] = None,
        timestamp: Optional[datetime] = None,
        original_exception: Optional[Exception] = None
    ):
        NormanError.__init__(self, message=message, details=details, timestamp=timestamp)
        self.original_exception = original_exception
