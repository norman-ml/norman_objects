from datetime import datetime, timezone


class NormanException(Exception):
    _norman_exception = True

    def __init__(
        self,
        status_code: int,
        error_type: str,
        message: str,
        cause: str,
        suggestions: list[str],
    ):
        super().__init__(message)
        self.timestamp = datetime.now(timezone.utc)
        self.status_code = status_code
        self.error_type = error_type
        self.message = message
        self.cause = cause
        self.suggestions = suggestions

    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "status_code": self.status_code,
            "error_type": self.error_type,
            "message": self.message,
            "cause": self.cause,
            "suggestions": self.suggestions
        }

    @staticmethod
    def to_norman_exception(e: Exception):
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
                    suggestions=exception_dict["suggestions"]
                )
                return exception

            message = str(e)
            exception = NormanException(
                status_code=500,
                error_type="Server",
                message="Norman encountered an error",
                cause=message,
                suggestions=[
                    "Try again in a few moments",
                    "Contact support if the problem persists",
                    "Check the service status page"
                ]
            )
            return exception
        except Exception as e:
            message = str(e)
            exception = NormanException(
                status_code=500,
                error_type="Configuration",
                message="Failed to create an exception due to malformed configuration",
                cause=message,
                suggestions=[
                    "Check that your configuration is correct.",
                    "Verify that your configuration has no missing fields."
                ]
            )
            return exception
