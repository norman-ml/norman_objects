from datetime import datetime, timezone
from typing import Annotated, Any

from pydantic import SerializerFunctionWrapHandler, ValidatorFunctionWrapHandler, WrapSerializer, WrapValidator


def datetime_serializer(value: Any, handler: SerializerFunctionWrapHandler):
    if isinstance(value, datetime) and value.tzinfo is None:
        value = value.astimezone(timezone.utc)

    value = handler(value)
    return value

def datetime_validator(value: Any, handler: ValidatorFunctionWrapHandler):
    value = handler(value)
    if isinstance(value, datetime) and value.tzinfo is None:
        value = value.astimezone(timezone.utc)

    return value

NormalizedDateTime = Annotated[
    datetime,
    WrapSerializer(datetime_serializer),
    WrapValidator(datetime_validator)
]
