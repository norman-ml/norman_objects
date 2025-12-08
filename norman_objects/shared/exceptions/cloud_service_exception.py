from norman_objects.shared.exceptions.norman_exception import NormanException


class CloudServiceException(NormanException):
    status_code: int = 500
    error_type: str = "cloud_service"

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

        self.status_code = CloudServiceException.status_code
        self.error_type = CloudServiceException.error_type
