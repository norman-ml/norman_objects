from typing import Optional
from contextvars import ContextVar
from norman_objects.tokens.access_token import AccessToken
from norman_objects.sensitive.sensitive_type import SensitiveType

class NormanContext:
    _access_token: ContextVar[Optional[AccessToken]] = ContextVar("norman_access_token", default=None)

    @staticmethod
    def get_access_token_object() -> Optional[AccessToken]:
        return NormanContext._access_token.get()

    @staticmethod
    def get_access_token():
        tok = NormanContext._access_token.get()
        return tok.get_access_token() if tok is not None else None  # returns SensitiveType(str) or None

    @staticmethod
    def get_decoded_access_token() -> Optional[dict]:
        tok = NormanContext._access_token.get()
        return tok.get_decoded_access_token() if tok is not None else None

    @staticmethod
    def set_access_token(access_token: AccessToken) -> None:
        NormanContext._access_token.set(access_token)

    @staticmethod
    def clear() -> None:
        NormanContext._access_token.set(None)
