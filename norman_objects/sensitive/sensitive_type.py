from typing import Type, TypeVar
from norman_objects.sensitive.sensitive import Sensitive

_sensitive_type_cache = {}

T = TypeVar("T")

class SensitiveType:
    def __new__(cls, inner_type: Type[T]) -> Type[Sensitive[T]]:
        if inner_type in _sensitive_type_cache:
            return _sensitive_type_cache[inner_type]

        class SensitiveCls(Sensitive, inner_type):
            pass

        SensitiveCls.__name__ = f"Sensitive|{inner_type.__name__.capitalize()}"
        _sensitive_type_cache[inner_type] = SensitiveCls

        return SensitiveCls
