from typing import Optional

from norman_objects.shared.errors.norman_error import NormanError


class NormanApiError(NormanError):
    status_code: int
    error_type: str
    suggestions: list[str] = []
    request_id: Optional[str] = None

    @classmethod
    def from_request(
        cls,
        message: str,
        details: dict,
        request_id: Optional[str]
    ):
        return cls(
            message=message,
            details=details,
            request_id=request_id
        )
