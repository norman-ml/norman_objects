from norman_objects.shared.exceptions.norman_exception import NormanException


class ValidationException(NormanException):
    status_code: int = 400
    error_type: str = "validation"

    def __init__(
            self,
            message: str,
            cause: str,
            suggestions: list[str],
            *args,
            **kwargs
    ):

        super().__init__(
            status_code=self.status_code,
            error_type=self.error_type,
            message=message,
            cause=cause,
            suggestions=suggestions,
            *args,
            **kwargs
        )

        self.status_code = ValidationException.status_code
        self.error_type = ValidationException.error_type
