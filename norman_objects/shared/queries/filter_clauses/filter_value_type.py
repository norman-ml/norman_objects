from typing import Union
from typing_extensions import TypeAlias

FilterTypeValue: TypeAlias = Union[str, int, float]
FilterTypeCollection: TypeAlias = Union[list[FilterTypeValue], set[FilterTypeValue], tuple[FilterTypeValue]]
FilterTypeVar: TypeAlias = Union[FilterTypeValue, FilterTypeCollection]
