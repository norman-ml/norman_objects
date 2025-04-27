def Sensitive(value=None):
    setattr(value, "__sensitive__", True)
    return value
