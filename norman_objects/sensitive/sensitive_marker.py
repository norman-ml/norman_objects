from pydantic import Field
from typing import Any

def Sensitive(default: Any = ..., **kwargs):
    return Field(default, sensitive=True, **kwargs)
