from typing import Generic, TypeVar, Union, Any

from pydantic import TypeAdapter, GetCoreSchemaHandler
from pydantic_core import core_schema

T = TypeVar("T")

class Sensitive(Generic[T]):
    __redacted_place_holder = "<redacted>"
    __sensitive__ = True

    def __init__(self, value: Union[T, "Sensitive[T]"]):
        self._value: T = Sensitive._get_plain_value(value)

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler: GetCoreSchemaHandler):
        (inner_type,) = source_type.__args__

        # TODO: investigate pydantic plain_validator_function to avoid redeclaring validate_sensitive()
        def validate_sensitive(value: Union[T, "Sensitive[T]"], info: core_schema.ValidationInfo) -> "Sensitive[T]":
            raw_value = Sensitive._get_plain_value(value)

            return cls(
                TypeAdapter(inner_type).validate_python(raw_value)
            )

        return core_schema.with_info_plain_validator_function(
            validate_sensitive,
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda sensitive: sensitive.value(),
                return_schema=handler(inner_type),
                when_used="always"
            )
        )

    @staticmethod
    def _get_plain_value(value):
        if isinstance(value, Sensitive):
            return value.value()

        return value

    def value(self) -> T:
        return self._value

    def __iter__(self):
        return iter(str(self))

    def dict(self):
        return self.__redacted_place_holder

    def json(self):
        return self.__redacted_place_holder

    def __str__(self):
        return self.__redacted_place_holder

    def __repr__(self):
        return self.__redacted_place_holder

    def __bytes__(self):
        return self.__redacted_place_holder.encode("utf-8")

    def __format__(self, format_spec):
        return self.__redacted_place_holder

    def __reduce__(self):
        return str, (self.__redacted_place_holder,)

    def __hash__(self):
        return hash(self._value)

    def __eq__(self, other):
        if isinstance(other, Sensitive):
            return self._value == other._value
        return self._value == other

    def __lt__(self, other):
        if isinstance(other, Sensitive):
            return self._value < other.value
        return self._value < other

    def __le__(self, other):
        if isinstance(other, Sensitive):
            return self._value <= other.value
        return self._value <= other

    def __gt__(self, other):
        if isinstance(other, Sensitive):
            return self._value > other.value
        return self._value > other

    def __ge__(self, other):
        if isinstance(other, Sensitive):
            return self._value >= other.value
        return self._value >= other

    def __add__(self, other):
        if isinstance(other, Sensitive):
            return self._value + other.value
        return self._value + other

    def __radd__(self, other):
        if isinstance(other, Sensitive):
            return other.value + self._value
        return other + self._value

    def __sub__(self, other):
        if isinstance(other, Sensitive):
            return self._value - other.value
        return self._value - other

    def __rsub__(self, other):
        if isinstance(other, Sensitive):
            return other.value - self._value
        return other - self._value

    def __mul__(self, other):
        if isinstance(other, Sensitive):
            return self._value * other.value
        return self._value * other

    def __rmul__(self, other):
        if isinstance(other, Sensitive):
            return other.value * self._value
        return other * self._value

    def __truediv__(self, other):
        if isinstance(other, Sensitive):
            return self._value / other.value
        return self._value / other

    def __rtruediv__(self, other):
        if isinstance(other, Sensitive):
            return other.value / self._value
        return other / self._value

    def __floordiv__(self, other):
        if isinstance(other, Sensitive):
            return self._value // other.value
        return self._value // other

    def __rfloordiv__(self, other):
        if isinstance(other, Sensitive):
            return other.value // self._value
        return other // self._value

    def __mod__(self, other):
        if isinstance(other, Sensitive):
            return self._value % other.value
        return self._value % other

    def __rmod__(self, other):
        if isinstance(other, Sensitive):
            return other.value % self._value
        return other % self._value

    def __pow__(self, other):
        if isinstance(other, Sensitive):
            return self._value ** other.value
        return self._value ** other

    def __rpow__(self, other):
        if isinstance(other, Sensitive):
            return other.value ** self._value
        return other ** self._value

    def __neg__(self):
        return -self._value

    def __pos__(self):
        return +self._value

    def __abs__(self):
        return abs(self._value)

    def __invert__(self):
        return ~self._value

    def __divmod__(self, other):
        if isinstance(other, Sensitive):
            return divmod(self._value, other.value)
        return divmod(self._value, other)

    def __rdivmod__(self, other):
        if isinstance(other, Sensitive):
            return divmod(other.value, self._value)
        return divmod(other, self._value)
