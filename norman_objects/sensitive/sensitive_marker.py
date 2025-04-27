def Sensitive(*, default=None):
    setattr(default, "__sensitive__", True)
    return default
