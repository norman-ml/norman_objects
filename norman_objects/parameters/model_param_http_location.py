from enum import Enum


class ModelParamHttpLocation(str, Enum):
    Body = "Body"
    Path = "Path"
    Query = "Query"