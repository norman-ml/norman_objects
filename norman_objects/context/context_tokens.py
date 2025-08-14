from contextvars import ContextVar
from typing import Optional

from norman_objects.tokens.access_token import AccessToken


class NormanContext:
    _access_token: ContextVar[Optional[AccessToken]] = ContextVar("norman_access_token", default=None)

    @staticmethod
    def get_context_token():
        return NormanContext._access_token.get()

    @staticmethod
    def set_context_token(access_token: AccessToken): #returns the decoded version of set context
        NormanContext._access_token.set(access_token)
        return NormanContext._access_token.get().get_decoded_access_token()

    @staticmethod
    def clear():
        NormanContext._access_token.set(None)
