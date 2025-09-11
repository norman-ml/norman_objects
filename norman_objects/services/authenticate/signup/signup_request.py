from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel


class SignupRequest(NormanBaseModel):
    device_id: Optional[str] = None
