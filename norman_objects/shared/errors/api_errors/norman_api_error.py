from datetime import datetime, UTC

from norman_objects.shared.errors.norman_error import NormanError


class NormanApiError(NormanError):

    status_code: int = 500
    error_type: str = "api_error"

    def __init__(
        self,
        message: str,
        context: dict = None,
        timestamp: datetime = None,
        suggestions: list[str] = None
    ):

        NormanError.__init__(
            self,
            message=message,
            context=context if context is not None else {},
            timestamp=timestamp if timestamp is not None else datetime.now(UTC)
        )

        self.suggestions = suggestions if suggestions is not None else []

    def to_dict(self) -> dict:

        return {
            "message": self.message,
            "status_code": self.status_code,
            "error_type": self.error_type,
            "context": self.context,
            "suggestions": self.suggestions,
            "timestamp": self.timestamp.isoformat()
        }
