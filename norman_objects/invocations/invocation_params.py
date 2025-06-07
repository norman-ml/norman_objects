from typing import List

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType


class InvocationParams(NormanBaseModel):
    access_token: SensitiveType(str)
    model_id: str
    invocation_id: str
    input_ids: List[str]
