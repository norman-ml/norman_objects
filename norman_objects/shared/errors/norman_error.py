from datetime import datetime, UTC
from typing import Optional


class NormanError(Exception):

    def __init__(
        self,
        message: str,
        context: Optional[dict] = None,
        timestamp: Optional[datetime] = None
    ):
        Exception.__init__(self, message)
        self.message = message
        self.context = context if context is not None else {}
        self.timestamp = timestamp if timestamp is not None else datetime.now(UTC)
