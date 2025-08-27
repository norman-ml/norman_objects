import base64
import json

from pydantic import Field, validator

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType


class JwtToken(NormanBaseModel):
    header: dict= Field(default_factory=dict)
    payload: dict = Field(default_factory=dict)
    encoded_signature: SensitiveType(str)

    @property
    def encoded(self):
        header_json = json.dumps(self.header, separators=(",", ":")).replace("/", "\\/")
        payload_json = json.dumps(self.payload, separators=(",", ":")).replace("/", "\\/")

        header_b64 = base64.urlsafe_b64encode(header_json.encode("utf-8")).rstrip(b"=").decode("utf-8")
        payload_b64 = base64.urlsafe_b64encode(payload_json.encode("utf-8")).rstrip(b"=").decode("utf-8")

        return f"{header_b64}.{payload_b64}.{self.encoded_signature.value()}"
