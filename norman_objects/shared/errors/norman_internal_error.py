from typing import Optional

from norman_objects.shared.errors.norman_error import NormanError


class NormanInternalError(NormanError):
    original_exception: Optional[Exception] = None
