from typing import Any, Dict, Callable

from pydantic import Field, PrivateAttr

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType


class AccessToken(NormanBaseModel):
    header: dict= Field(default_factory=dict)
    payload: dict = Field(default_factory=dict)
    signature: SensitiveType(str)

    def __init__(
            self,
            header: dict,
            payload: dict,
            signature: str,
            **kwargs: Any
    ):
        super().__init__(
            header=header or {},
            payload=payload or {},
            signature=SensitiveType(str)(signature),
            **kwargs
        )

    @classmethod
    def initialize_from_dict(cls, decoded_access_token_dict: dict):
        return cls(
            header=decoded_access_token_dict.get("header"),
            payload=decoded_access_token_dict.get("payload"),
            signature=SensitiveType(str)(decoded_access_token_dict.get("signature"))
        )

    def get_decoded_access_token(self):
        return {"header": self.header, "payload": self.payload, "signature": self.signature}

    def set_decoded_access_token(self, header:dict, payload:dict, signature:SensitiveType):

        self.header = header
        self.payload = payload
        self.signature = signature

        return self
