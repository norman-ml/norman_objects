from typing import TypeAlias, Union

FilterTypeValue: TypeAlias = Union[str, int, float]
FilterTypeVar: TypeAlias = Union[FilterTypeValue, list[FilterTypeValue]]
