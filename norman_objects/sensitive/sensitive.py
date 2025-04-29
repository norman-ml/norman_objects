# pure python
class Sensitive:
    __redacted_place_holder = "<redacted>"

    def __init__(self, value):
        self._value = value
        self.__sensitive__ = True

    def __iter__(self):
        return iter(str(self))

    def value(self):
        return self._value

    def dict(self):
        return self.__redacted_place_holder

    def json(self):
        return self.__redacted_place_holder

    def __str__(self):
        return self.__redacted_place_holder

    def __repr__(self):
        return self.__redacted_place_holder

    def __bytes__(self):
        return bytes(self.__redacted_place_holder)

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
        return self._value < (other._value if isinstance(other, Sensitive) else other)

    def __le__(self, other):
        return self._value <= (other._value if isinstance(other, Sensitive) else other)

    def __gt__(self, other):
        return self._value > (other._value if isinstance(other, Sensitive) else other)

    def __ge__(self, other):
        return self._value >= (other._value if isinstance(other, Sensitive) else other)

    def __add__(self, other):
        return self._value + (other._value if isinstance(other, Sensitive) else other)

    def __radd__(self, other):
        return (other._value if isinstance(other, Sensitive) else other) + self._value

    def __sub__(self, other):
        return self._value - (other._value if isinstance(other, Sensitive) else other)

    def __rsub__(self, other):
        return (other._value if isinstance(other, Sensitive) else other) - self._value

    def __mul__(self, other):
        return self._value * (other._value if isinstance(other, Sensitive) else other)

    def __rmul__(self, other):
        return (other._value if isinstance(other, Sensitive) else other) * self._value

    def __truediv__(self, other):
        return self._value / (other._value if isinstance(other, Sensitive) else other)

    def __rtruediv__(self, other):
        return (other._value if isinstance(other, Sensitive) else other) / self._value

    def __floordiv__(self, other):
        return self._value // (other._value if isinstance(other, Sensitive) else other)

    def __rfloordiv__(self, other):
        return (other._value if isinstance(other, Sensitive) else other) // self._value

    def __mod__(self, other):
        return self._value % (other._value if isinstance(other, Sensitive) else other)

    def __rmod__(self, other):
        return (other._value if isinstance(other, Sensitive) else other) % self._value

    def __pow__(self, other):
        return self._value ** (other._value if isinstance(other, Sensitive) else other)

    def __rpow__(self, other):
        return (other._value if isinstance(other, Sensitive) else other) ** self._value

    def __neg__(self):
        return -self._value

    def __pos__(self):
        return +self._value

    def __abs__(self):
        return abs(self._value)

    def __invert__(self):
        return ~self._value

    def __divmod__(self, other):
        return divmod(self._value, other._value if isinstance(other, Sensitive) else other)

    def __rdivmod__(self, other):
        return divmod(other._value if isinstance(other, Sensitive) else other, self._value)
