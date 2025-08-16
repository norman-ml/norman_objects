import base64
import json

from pydantic import Field, validator

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType


class AccessToken(NormanBaseModel):
    header: dict= Field(default_factory=dict)
    payload: dict = Field(default_factory=dict)
    signature: SensitiveType(str)

    @validator("signature", pre=True)
    def signature_validation(cls, signature):
        if isinstance(signature, SensitiveType(str)):
            return signature
        else:
            return SensitiveType(str)(signature)

    def get_encoded(self):
        header_json = json.dumps(self.header, separators=(",", ":"), ensure_ascii=False).replace("/", "\\/")
        payload_json = json.dumps(self.payload, separators=(",", ":"), ensure_ascii=False).replace("/", "\\/")

        header_b64 = base64.urlsafe_b64encode(header_json.encode("utf-8")).rstrip(b"=").decode("ascii")
        payload_b64 = base64.urlsafe_b64encode(payload_json.encode("utf-8")).rstrip(b"=").decode("ascii")

        return f"{header_b64}.{payload_b64}.{self.signature.value()}"
