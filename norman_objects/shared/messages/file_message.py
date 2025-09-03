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
