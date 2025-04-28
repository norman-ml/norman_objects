from norman_objects.sensitive.sensitive import Sensitive

_sensitive_type_cache = {}


def SensitiveType(inner_type):
    if inner_type in _sensitive_type_cache:
        return _sensitive_type_cache[inner_type]

    else:
        class SensitiveCls(inner_type, Sensitive):
            pass

        SensitiveCls.__name__ = f"Sensitive|{inner_type.__name__.capitalize()}"
        _sensitive_type_cache[inner_type] = SensitiveCls

        return SensitiveCls
