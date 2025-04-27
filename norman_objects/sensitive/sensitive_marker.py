class SensitiveMarker:
    __sensitive__ = True

def Sensitive(*, default=None):
    if default is None:
        return SensitiveMarker()
    setattr(default, "__sensitive__", True)
    return default
