from typing import Any

from pydantic import Field, validator

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType


class AccessToken(NormanBaseModel):
    header: dict= Field(default_factory=dict)
    payload: dict = Field(default_factory=dict)
    signature: SensitiveType(str)

    @validator("signature", pre=True)
    def signature_validation(cls, signature: Any):
        if isinstance(signature, SensitiveType(str)):
            return signature
        else:
            return SensitiveType(str)(signature)
