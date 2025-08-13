from typing import Any, Dict, Callable, Tuple

from pydantic import Field, PrivateAttr

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType

EncodeFn = Callable[[Dict[str, Any], Dict[str, Any], SensitiveType], str]
DecodeFn = Callable[[str], Tuple[Dict[str, Any], Dict[str, Any], SensitiveType]]

class AccessToken(NormanBaseModel):
    header: Dict[str, Any] = Field(default_factory=dict)
    payload: Dict[str, Any] = Field(default_factory=dict)
    hmac: SensitiveType = SensitiveType(str)

    # not part of schema/serialization
    _jwt_encode: EncodeFn = PrivateAttr()
    _jwt_decode: DecodeFn = PrivateAttr()

    class Config:
        arbitrary_types_allowed = True  # allow callables & SensitiveType - what is this

    def __init__(
        self,
        *,
        jwt_encode: EncodeFn,
        jwt_decode: DecodeFn,
        cleartext_access_token: str
    ):

        decoded_token = jwt_decode(cleartext_access_token)
        header = decoded_token["header"]
        payload = decoded_token["payload"]
        hmac = decoded_token["hmac"]

        super().__init__(header=header, payload=payload, hmac=hmac)
        self._jwt_encode = jwt_encode
        self._jwt_decode = jwt_decode

    def get_access_token(self):
        encoded_access_token = self._jwt_encode(self.header, self.payload, self.hmac)
        return SensitiveType(str)(encoded_access_token)

    def get_decoded_access_token(self):
        return {
            "header": self.header,
            "payload": self.payload,
            "hmac": self.hmac
        }