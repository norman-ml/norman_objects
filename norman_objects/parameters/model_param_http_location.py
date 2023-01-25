from enum import Enum


class ModelParamHttpLocation(Enum):
    Body = "Body"
    Path = "Path"
    Query = "Query"