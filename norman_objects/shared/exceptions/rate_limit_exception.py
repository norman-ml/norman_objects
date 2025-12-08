from norman_objects.shared.exceptions.norman_exception import NormanException


class RateLimitException(NormanException):
    status_code: int = 429
    error_type: str = "rate_limit"

    def __init__(
            self,
            message: str,
            cause: str,
            suggestions: list[str]
    ):

        super().__init__(
            status_code=self.status_code,
            error_type=self.error_type,
            message=message,
            cause=cause,
            suggestions=suggestions
        )
