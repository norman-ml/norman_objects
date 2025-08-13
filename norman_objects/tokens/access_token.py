from typing import Any, Dict, Callable

from pydantic import Field, PrivateAttr

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType

EncodeFn = Callable[[Dict[str, Any], Dict[str, Any], str], str]
DecodeFn = Callable[[str], Dict[str, Any]]           # returns dict as above

class AccessToken(NormanBaseModel):
    header: Dict[str, Any] = Field(default_factory=dict)   # optional for logs
    payload: Dict[str, Any] = Field(default_factory=dict)
    hmac: SensitiveType(str)

    _encode_token: EncodeFn = PrivateAttr()
    _decode_token: DecodeFn = PrivateAttr()

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, *, jwt_encode: EncodeFn, jwt_decode: DecodeFn, cleartext_access_token: str):
        parts = jwt_decode(cleartext_access_token)
        super().__init__(
            header=parts["header"],
            payload=parts["payload"],
            hmac=SensitiveType(str)(parts["hmac"])
        )
        self._encode_token = jwt_encode
        self._decode_token = jwt_decode

    def get_access_token(self):
        encoded_access_token = self._encode_token(
            self.header,
            self.payload,
            self.hmac.value()
        )
        return SensitiveType(str)(encoded_access_token)

    def get_decoded_access_token(self):
        return {"header": self.header, "payload": self.payload, "hmac": self.hmac}
