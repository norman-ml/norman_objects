from typing import Any, Dict, Callable
from pydantic import Field, PrivateAttr
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType

EncodeFn = Callable[[Dict[str, Any], Dict[str, Any], str], str]
DecodeFn = Callable[[str], Dict[str, Any]]           # returns dict as above

class AccessToken(NormanBaseModel):
    header_b64: str
    payload_b64: str
    hmac: SensitiveType(str)
    header: Dict[str, Any] = Field(default_factory=dict)   # optional for logs
    payload: Dict[str, Any] = Field(default_factory=dict)

    _jwt_encode: EncodeFn = PrivateAttr()
    _jwt_decode: DecodeFn = PrivateAttr()

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, *, jwt_encode: EncodeFn, jwt_decode: DecodeFn, cleartext_access_token: str):
        parts = jwt_decode(cleartext_access_token)
        super().__init__(
            header_b64=parts["header_b64"],
            payload_b64=parts["payload_b64"],
            hmac=SensitiveType(str)(parts["hmac"]),
            header=parts["header"],
            payload=parts["payload"],
        )
        self._jwt_encode = jwt_encode
        self._jwt_decode = jwt_decode

    def get_access_token(self):
        return SensitiveType(str)(f"{self.header_b64}.{self.payload_b64}.{self.hmac.value()}")

    def get_access_token2(self):
        encoded_access_token = self._jwt_encode(
            self.header,
            self.payload,
            self.hmac.value()  # unwrap Sensitive -> str
        )
        return SensitiveType(str)(encoded_access_token)

    def get_decoded_access_token(self) -> Dict[str, Any]:
        return {"header": self.header, "payload": self.payload, "hmac": self.hmac}
