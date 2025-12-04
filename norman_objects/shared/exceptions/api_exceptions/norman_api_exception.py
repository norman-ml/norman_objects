from norman_objects.shared.exceptions.norman_exception import NormanException


class NormanApiException(NormanException):

    def __init__(
        self,
        message: str,
        status_code: int,
        error_type: str,
        suggestions: list[str]
    ):

        super().__init__(
            message=message,
        )

        self.status_code = status_code
        self.error_type = error_type
        self.suggestions = suggestions

    def to_dict(self):
        return {
            "message": super().message,
            "timestamp": super().timestamp.isoformat(),
            "status_code": self.status_code,
            "error_type": self.error_type,
            "suggestions": self.suggestions
        }
