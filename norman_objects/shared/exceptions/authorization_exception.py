from norman_objects.shared.exceptions.norman_exception import NormanException


class AuthorizationException(NormanException):
    status_code: int = 403
    error_type: str = "authorization"

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

        self.status_code = AuthorizationException.status_code
        self.error_type = AuthorizationException.error_type
