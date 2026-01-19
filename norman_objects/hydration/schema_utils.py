from typing import Any, Dict, Optional, Type, Union

from pydantic import BaseModel
from pydantic.fields import FieldInfo

from norman_objects.hydration.id_markers import GeneratedId, DerivedId


class SchemaUtils:
    @staticmethod
    def get_id_marker(field_info: FieldInfo) -> Optional[Union[GeneratedId, DerivedId]]:
        for metadata in field_info.metadata:
            if isinstance(metadata, (GeneratedId, DerivedId)):
                return metadata
        return None

    @staticmethod
    def is_id_field(field_info: FieldInfo) -> bool:
        return SchemaUtils.get_id_marker(field_info) is not None

    @staticmethod
    def get_id_markers(model_class: Type[BaseModel]) -> Dict[str, Union[GeneratedId, DerivedId]]:
        markers: Dict[str, Union[GeneratedId, DerivedId]] = {}

        for field_name, field_info in model_class.model_fields.items():
            marker = SchemaUtils.get_id_marker(field_info)
            if marker is not None:
                markers[field_name] = marker

        return markers

    @staticmethod
    def get_model_class(create_schema_instance: Any):
        return getattr(create_schema_instance, "_norman_model_class", None)
