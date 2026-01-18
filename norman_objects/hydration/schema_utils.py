from typing import Any, Dict, Optional, Type, Union

from pydantic import BaseModel
from pydantic.fields import FieldInfo

from norman_objects.hydration.id_markers import GeneratedId, DerivedId


def get_id_markers(model_class: Type[BaseModel]) -> Dict[str, Union[GeneratedId, DerivedId]]:
    markers: Dict[str, Union[GeneratedId, DerivedId]] = {}

    for field_name, field_info in model_class.model_fields.items():
        marker = _get_id_marker(field_info)
        if marker is not None:
            markers[field_name] = marker

    return markers


def _get_id_marker(field_info: FieldInfo) -> Optional[Union[GeneratedId, DerivedId]]:
    for metadata in field_info.metadata:
        if isinstance(metadata, (GeneratedId, DerivedId)):
            return metadata
    return None


def get_full_model_class(create_schema_instance: Any) -> Optional[Type[BaseModel]]:
    return getattr(create_schema_instance, "_norman_full_model_class", None)
