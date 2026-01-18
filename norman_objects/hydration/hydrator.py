from typing import Any, Callable, Dict, Optional

from norman_objects.hydration.id_markers import GeneratedId, DerivedId
from norman_objects.hydration.schema_utils import get_id_markers, get_full_model_class


def hydrate(
    create_schema_instance: Any,
    id_generator: Callable[[], str],
    context: Optional[Dict[str, str]] = None
) -> Any:
    context = context.copy() if context else {}

    full_model_class = get_full_model_class(create_schema_instance)
    if full_model_class is None:
        return create_schema_instance

    id_markers = get_id_markers(full_model_class)

    field_values = _generate_ids(id_markers, context, id_generator)
    field_values.update(_derive_ids(id_markers, context))
    field_values.update(_hydrate_fields(create_schema_instance, context, id_generator))

    return full_model_class(**field_values)


def _generate_ids(
    id_markers: Dict[str, Any],
    context: Dict[str, str],
    id_generator: Callable[[], str]
) -> Dict[str, str]:
    field_values = {}

    for field_name, marker in id_markers.items():
        if isinstance(marker, GeneratedId):
            new_id = id_generator()
            field_values[field_name] = new_id
            context_key = marker.context_key or field_name
            context[context_key] = new_id

    return field_values


def _derive_ids(id_markers: Dict[str, Any], context: Dict[str, str]) -> Dict[str, str]:
    field_values = {}

    for field_name, marker in id_markers.items():
        if isinstance(marker, DerivedId):
            if marker.source not in context:
                raise ValueError(
                    f"Cannot derive '{field_name}': source '{marker.source}' not in context. "
                    f"Available: {list(context.keys())}"
                )
            field_values[field_name] = context[marker.source]

    return field_values


def _hydrate_fields(
    create_schema_instance: Any,
    context: Dict[str, str],
    id_generator: Callable[[], str]
) -> Dict[str, Any]:
    field_values = {}

    for field_name in create_schema_instance.model_fields:
        value = getattr(create_schema_instance, field_name)
        _propagate_to_context(field_name, value, context)
        field_values[field_name] = _hydrate_value(value, context, id_generator)

    return field_values


def _propagate_to_context(field_name: str, value: Any, context: Dict[str, str]) -> None:
    if isinstance(value, str) and value and field_name not in context:
        context[field_name] = value


def _hydrate_value(
    value: Any,
    context: Dict[str, str],
    id_generator: Callable[[], str]
) -> Any:
    if value is None:
        return None

    if _is_create_schema(value):
        return hydrate(value, id_generator, context)

    if isinstance(value, list):
        return [_hydrate_value(item, context, id_generator) for item in value]

    if isinstance(value, dict):
        return {k: _hydrate_value(v, context, id_generator) for k, v in value.items()}

    return value


def _is_create_schema(value: Any) -> bool:
    return hasattr(value, "_norman_full_model_class")
