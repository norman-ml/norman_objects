from datetime import datetime, UTC
from typing import Optional


class NormanError(Exception):
    def __init__(
        self,
        message: str,
        details: Optional[dict] = None,
        timestamp: Optional[datetime] = None
    ):
        super().__init__(message)
        self.message = message
        self.details = details if details is not None else {}
        self.timestamp = timestamp if timestamp is not None else datetime.now(UTC)
