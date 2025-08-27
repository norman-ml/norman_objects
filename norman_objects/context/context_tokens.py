from contextvars import ContextVar
from typing import Optional

from norman_objects.authorization.access_token import JwtToken


class NormanAccessContext:
    _access_token: ContextVar[Optional[JwtToken]] = ContextVar("norman_access_token")

    @staticmethod
    def get_access_token():
        return NormanAccessContext._access_token.get()

    @staticmethod
    def set_access_token(access_token: JwtToken):
        NormanAccessContext._access_token.set(access_token)

    @staticmethod
    def clear():
        NormanAccessContext._access_token.set(None)
