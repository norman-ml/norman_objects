from datetime import datetime
from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.errors.error_type import ErrorType


class ErrorResponse(NormanBaseModel):

    error_type: ErrorType
    message: str
    status_code: int
    details: Optional[dict] = None
    suggestions: Optional[list[str]] = None
    request_id: Optional[str] = None
    timestamp: Optional[datetime] = None
