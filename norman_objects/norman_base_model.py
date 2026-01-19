from typing import Any, Dict, Optional, Tuple, Type, Union, get_args, get_origin

from pydantic import BaseModel, Field, create_model
from pydantic.fields import FieldInfo
from pydantic_core import PydanticUndefined

from norman_objects.norman_update_schema import NormanUpdateSchema
from norman_objects.norman_create_schema import NormanCreateSchema
from norman_objects.hydration.schema_utils import SchemaUtils


class NormanBaseModel(BaseModel):

    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs):
        cls.UpdateSchema: Type[BaseModel] = create_model(
            f"{cls.__name__}Update",
            **{
                name: (Optional[field.annotation], None)
                for name, field in cls.model_fields.items()
            },
            __base__=NormanUpdateSchema,
        )

        cls.CreateSchema: Type[BaseModel] = cls._generate_create_schema()

    @classmethod
    def _generate_create_schema(cls):
        create_schema_fields: Dict[str, Tuple[Any, Any]] = {}

        for field_name, field_info in cls.model_fields.items():
            if SchemaUtils.is_id_field(field_info):
                continue

            source_field_type = field_info.annotation
            transformed_field_type = cls._transform_nested_types(source_field_type)
            field_default_value = cls._resolve_field_default_value(field_info)
            create_schema_fields[field_name] = (transformed_field_type, field_default_value)

        schema_class = create_model(
            f"{cls.__name__}Create",
            __base__=NormanCreateSchema,
            **create_schema_fields
        )

        schema_class._norman_model_class = cls
        return schema_class

    @staticmethod
    def _resolve_field_default_value(field_info: FieldInfo):
        if field_info.default_factory is not None:
            return Field(default_factory=field_info.default_factory)

        if field_info.default is not PydanticUndefined:
            return field_info.default

        return ...

    @classmethod
    def _transform_nested_types(cls, field_type: Any) -> Any:
        if field_type is None or field_type is type(None):
            return field_type

        origin = get_origin(field_type)

        if origin is Union:
            args = get_args(field_type)
            none_type = type(None)
            non_none_args = [a for a in args if a is not none_type]
            has_none = none_type in args

            if has_none and len(non_none_args) == 1:
                transformed_nested_field = cls._transform_nested_types(non_none_args[0])
                return Optional[transformed_nested_field]
            else:
                transformed_args = tuple(cls._transform_nested_types(a) for a in args)
                return Union[transformed_args]

        if origin is list:
            args = get_args(field_type)
            if args:
                transformed_nested_field = cls._transform_nested_types(args[0])
                return list[transformed_nested_field]
            return field_type

        if origin is dict:
            args = get_args(field_type)
            if len(args) >= 2:
                key_type = args[0]
                value_type = cls._transform_nested_types(args[1])
                return dict[key_type, value_type]
            return field_type

        if cls._is_norman_base_model(field_type):
            if hasattr(field_type, 'CreateSchema'):
                return field_type.CreateSchema
            return field_type

        return field_type

    @staticmethod
    def _is_norman_base_model(annotation: Any):
        try:
            return (
                isinstance(annotation, type) and
                issubclass(annotation, NormanBaseModel) and
                annotation is not NormanBaseModel
            )
        except TypeError:
            return False
