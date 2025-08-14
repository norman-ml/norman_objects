try:
    from typing import TypeAlias, Union
except ImportError:
    from typing_extensions import TypeAlias
    from typing import Union

FilterTypeValue: TypeAlias = Union[str, int, float]
FilterTypeVar: TypeAlias = Union[FilterTypeValue, list[FilterTypeValue]]
