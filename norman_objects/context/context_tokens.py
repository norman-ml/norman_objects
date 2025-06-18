from contextvars import ContextVar

from norman_objects.sensitive.sensitive_type import SensitiveType

class NormanContext:
    raw_access_token: ContextVar[SensitiveType(str)] = ContextVar("norman_raw_access_token", default=None)
    decoded_access_token: ContextVar[SensitiveType(dict)] = ContextVar("norman_decoded_access_token", default=None)
