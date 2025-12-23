from datetime import datetime, timezone
from typing import Optional
import opentelemetry.trace

class NormanException(Exception):
    _norman_exception = True

    def __init__(
        self,
        status_code: int,
        error_type: str,
        message: str,
        cause: str,
        suggestions: list[str],
        trace_id: Optional[str] = None
    ):
        super().__init__(message)
        self.timestamp = datetime.now(timezone.utc)
        self.status_code = status_code
        self.error_type = error_type
        self.message = message
        self.cause = cause
        self.suggestions = suggestions

        if trace_id is None:
            current_span = opentelemetry.trace.get_current_span()
            span_context = current_span.get_span_context()
            if span_context.is_valid:
                self.trace_id = format(span_context.trace_id, '032x')
            else:
                self.trace_id = "0"
        else:
            self.trace_id = trace_id


    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "status_code": self.status_code,
            "error_type": self.error_type,
            "message": self.message,
            "cause": self.cause,
            "suggestions": self.suggestions,
            "trace_id": self.trace_id
        }

    @staticmethod
    def cast(e: Exception, message: Optional[str] = None):
        try:
            if isinstance(e, NormanException):
                return e

            exception_dict = False
            if e.args is not None and len(e.args) > 0:
                exception_dict = e.args[0]

            if isinstance(exception_dict, dict):
                exception = NormanException(
                    status_code=exception_dict["status_code"],
                    error_type=exception_dict["error_type"],
                    message=exception_dict["message"],
                    cause=exception_dict["cause"],
                    suggestions=exception_dict["suggestions"],
                    trace_id=exception_dict["trace_id"]
                )
                return exception

            cause = str(e)
            if message is None:
                message = "Norman encountered an error"

            exception = NormanException(
                status_code=500,
                error_type="Server",
                message=message,
                cause=cause,
                suggestions=[
                    "Try again in a few moments",
                    "Contact support if the problem persists",
                    "Check the service status page"
                ]
            )
            return exception
        except Exception as e:
            cause = str(e)
            exception = NormanException(
                status_code=500,
                error_type="Configuration",
                message="Failed to create an exception due to malformed configuration",
                cause=cause,
                suggestions=[
                    "Check that your configuration is correct.",
                    "Verify that your configuration has no missing fields."
                ]
            )
            return exception
