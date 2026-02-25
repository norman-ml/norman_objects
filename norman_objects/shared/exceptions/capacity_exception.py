from norman_objects.shared.exceptions.norman_exception import NormanException


class CapacityException(NormanException):
    status_code: int = 402
    error_type: str = "capacity"

    def __init__(
            self,
            message: str,
            cause: str,
            suggestions: list[str],
    ):

        super().__init__(
            status_code=self.status_code,
            error_type=self.error_type,
            message=message,
            cause=cause,
            suggestions=suggestions
        )