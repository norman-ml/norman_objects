from typing import Any, Dict, Optional, Tuple, Type, Union, get_args, get_origin

from pydantic import BaseModel, Field, create_model
from pydantic.fields import FieldInfo
from pydantic_core import PydanticUndefined

from norman_objects.norman_update_schema import NormanUpdateSchema
from norman_objects.norman_create_schema import NormanCreateSchema
from norman_objects.hydration.id_markers import GeneratedId, DerivedId


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
    def _generate_create_schema(cls) -> Type[BaseModel]:
        create_fields: Dict[str, Tuple[Any, Any]] = {}

        for field_name, field_info in cls.model_fields.items():
            if cls._is_id_field(field_info):
                continue

            original_annotation = field_info.annotation
            transformed_annotation = cls._transform_annotation(original_annotation)
            default = cls._get_field_default(field_info)
            create_fields[field_name] = (transformed_annotation, default)

        schema_class = create_model(
            f"{cls.__name__}Create",
            __base__=NormanCreateSchema,
            **create_fields
        )

        schema_class._norman_full_model_class = cls
        return schema_class

    @staticmethod
    def _is_id_field(field_info: FieldInfo) -> bool:
        for metadata in field_info.metadata:
            if isinstance(metadata, (GeneratedId, DerivedId)):
                return True
        return False

    @staticmethod
    def _get_field_default(field_info: FieldInfo) -> Any:
        if field_info.default_factory is not None:
            return Field(default_factory=field_info.default_factory)

        if field_info.default is not PydanticUndefined:
            return field_info.default

        return ...

    @classmethod
    def _transform_annotation(cls, annotation: Any) -> Any:
        if annotation is None or annotation is type(None):
            return annotation

        origin = get_origin(annotation)

        if origin is Union:
            args = get_args(annotation)
            none_type = type(None)
            non_none_args = [a for a in args if a is not none_type]
            has_none = none_type in args

            if has_none and len(non_none_args) == 1:
                transformed_inner = cls._transform_annotation(non_none_args[0])
                return Optional[transformed_inner]
            else:
                transformed_args = tuple(cls._transform_annotation(a) for a in args)
                return Union[transformed_args]

        if origin is list:
            args = get_args(annotation)
            if args:
                transformed_inner = cls._transform_annotation(args[0])
                return list[transformed_inner]
            return annotation

        if origin is dict:
            args = get_args(annotation)
            if len(args) >= 2:
                key_type = args[0]
                value_type = cls._transform_annotation(args[1])
                return dict[key_type, value_type]
            return annotation

        if cls._is_norman_base_model(annotation):
            if hasattr(annotation, 'CreateSchema'):
                return annotation.CreateSchema
            return annotation

        return annotation

    @staticmethod
    def _is_norman_base_model(annotation: Any) -> bool:
        try:
            return (
                isinstance(annotation, type) and
                issubclass(annotation, NormanBaseModel) and
                annotation is not NormanBaseModel
            )
        except TypeError:
            return False
