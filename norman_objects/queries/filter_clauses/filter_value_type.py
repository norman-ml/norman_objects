from typing import Collection, TypeAlias

FilterTypeValue: TypeAlias = str | int | float
FilterTypeVar: TypeAlias = FilterTypeValue | Collection[FilterTypeValue]
