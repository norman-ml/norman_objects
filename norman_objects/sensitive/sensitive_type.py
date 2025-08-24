from typing import Type, TypeVar

from pydantic_core import core_schema

from norman_objects.sensitive.sensitive import Sensitive

_sensitive_type_cache = {}

T = TypeVar("T")

class SensitiveType:
    def __new__(cls, inner_type: Type[T]) -> Type[Sensitive[T]]:
        if inner_type in _sensitive_type_cache:
            return _sensitive_type_cache[inner_type]

        class SensitiveCls(Sensitive, inner_type):
            @classmethod
            def __get_pydantic_core_schema__(cls, _, handler):
                return core_schema.no_info_after_validator_function(
                    lambda v: cls(v),
                    handler.generate_schema(inner_type)
                )

        SensitiveCls.__name__ = f"Sensitive|{inner_type.__name__.capitalize()}"
        _sensitive_type_cache[inner_type] = SensitiveCls

        return SensitiveCls
