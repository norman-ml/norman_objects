from contextvars import ContextVar
from typing import Optional

from norman_objects.authorization.access_token import AccessToken


class NormanContext:
    _access_token: ContextVar[Optional[AccessToken]] = ContextVar("norman_access_token")

    @staticmethod
    def get_access_token():
        return NormanContext._access_token.get()

    @staticmethod
    def set_access_token(access_token: AccessToken):
        NormanContext._access_token.set(access_token)

    @staticmethod
    def clear():
        NormanContext._access_token.set(None)
