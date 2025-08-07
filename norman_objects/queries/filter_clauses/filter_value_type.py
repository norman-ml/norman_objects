from typing import TypeAlias

FilterTypeValue: TypeAlias = str | int | float
FilterTypeVar: TypeAlias = FilterTypeValue | list[FilterTypeValue]
