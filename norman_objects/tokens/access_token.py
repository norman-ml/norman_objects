from typing import Any, Dict, Callable

from pydantic import Field, PrivateAttr

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType


class AccessToken(NormanBaseModel):
    header: Dict[str, Any] = Field(default_factory=dict)
    payload: Dict[str, Any] = Field(default_factory=dict)
    hmac: SensitiveType(str)

    _encode_token: Callable[[Dict[str, Any], Dict[str, Any], str], str] = PrivateAttr()
    _decode_token: Callable[[str], dict] = PrivateAttr()

    class Config:
        arbitrary_types_allowed = True

    def __init__(
            self,
            *,
            encode_token: Callable[[Dict[str, Any], Dict[str, Any], str], str],
            decode_token: Callable[[str], Dict[str, Any]] = PrivateAttr(),
            encoded_access_token: str
    ):
        parts = decode_token(encoded_access_token)
        super().__init__(
            header=parts["header"],
            payload=parts["payload"],
            hmac=SensitiveType(str)(parts["hmac"]),
        )
        self._encode_token = encode_token
        self._decode_token = decode_token

    def initialize_from_decoded_token(
            cls,
            decoded: Dict[str, Any],
            *,
            encode_token: Callable[[Dict[str, Any], Dict[str, Any], str], str],
            decode_token: Callable[[str], Dict[str, Any]],
    ):
        header = decoded.get("header")
        payload = decoded.get("payload") or {}
        hmac = decoded.get("hmac")

        access_token = cls.construct(
            header=header,
            payload=payload,
            hmac=SensitiveType(str)(hmac),
        )
        access_token._encode_token = encode_token
        access_token._decode_token = decode_token
        return access_token

    def get_encoded_access_token(self):
        encoded_access_token = self._encode_token(
            self.header,
            self.payload,
            self.hmac.value()
        )
        return SensitiveType(str)(encoded_access_token)

    def get_decoded_access_token(self):
        return {"header": self.header, "payload": self.payload, "hmac": self.hmac}

    def set_access_token(self, encoded_access_token: str):
        parts = self._decode_token(encoded_access_token)

        self.header = parts.get("header") or {}
        self.payload = parts.get("payload") or {}
        self.hmac = SensitiveType(str)(parts.get("hmac"))

        return self
