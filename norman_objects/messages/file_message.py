from norman_objects.files.file_properties import FileProperties
from norman_objects.messages.norman_base_message import NormanBaseMessage


class FileMessage:
    """
        Pydantic allows inheritance only from a single BaseModel.
        This change forces every class that inherits from this class
        to define a file properties field
    """
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if "file_properties" not in getattr(cls, "__annotations__", {}):
            raise TypeError(
                f"{cls.__name__} must declare 'file_properties' field"
            )
