from typing import Optional

from pydantic import ConfigDict

from norman_objects.shared.errors.norman_error import NormanError
from norman_objects.shared.errors.ttttttt import NormanIntError


class NormanInternalError(NormanIntError):
    # model_config = ConfigDict(arbitrary_types_allowed=True)

    original_exception: Optional[Exception] = None
