from datetime import datetime, UTC
from typing import Optional

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.errors.norman_error import NormanError


class NormanApiError(NormanBaseModel, NormanError):
    message: str
    details: dict = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))

    status_code: int
    error_type: str
    suggestions: list[str] = Field(default_factory=list)
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
