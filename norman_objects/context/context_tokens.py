from contextvars import ContextVar
from norman_objects.sensitive.sensitive import Sensitive
from norman_objects.sensitive.sensitive_type import SensitiveType


class NormanContext:
    _access_token: ContextVar[SensitiveType(str)] = ContextVar("norman_access_token")
    _decoded_access_token: ContextVar[SensitiveType(str)] = ContextVar("norman_decoded_access_token")

    @staticmethod
    def get_access_token():
        return NormanContext._access_token.get(None)

    @staticmethod
    def set_access_token(token: Sensitive):
        NormanContext._access_token.set(token)

    @staticmethod
    def clear_access_token():
        NormanContext._access_token.set(None)

    @staticmethod
    def get_decoded_access_token():
        return NormanContext._decoded_access_token.get(None)

    @staticmethod
    def set_decoded_access_token(decoded: Sensitive):
        NormanContext._decoded_access_token.set(decoded)

    @staticmethod
    def clear_decoded_access_token():
        NormanContext._decoded_access_token.set(None)

    @staticmethod
    def clear():
        NormanContext.clear_access_token()
        NormanContext.clear_decoded_access_token()
