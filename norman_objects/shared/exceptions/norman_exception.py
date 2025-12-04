from datetime import datetime, timezone
from typing import Optional
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime


class NormanException(Exception):
    def __init__(
        self,
        message: str,
        context: Optional[dict] = None,
        timestamp: Optional[NormalizedDateTime] = None
    ):
        Exception.__init__(self, message)
        self.message = message

        if context is None:
            context = {}
        self.context = context

        if timestamp is None:
            timestamp = datetime.now(timezone.utc)
        self.timestamp = timestamp
