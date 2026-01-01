from contextvars import ContextVar
from typing import Optional

from norman_objects.shared.authorization.jwt_token import JwtToken


class NormanAccessContext:
    __access_token: ContextVar[Optional[JwtToken]] = ContextVar("norman_access_token")

    @staticmethod
    def get():
        return NormanAccessContext.__access_token.get()

    @staticmethod
    def set(access_token: JwtToken):
        NormanAccessContext.__access_token.set(access_token)

    @staticmethod
    def clear():
        NormanAccessContext.__access_token.set(None)
