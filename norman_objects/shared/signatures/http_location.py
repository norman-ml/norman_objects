from enum import Enum


class HttpLocation(str, Enum):
    Body = "Body"
    Path = "Path"
    Query = "Query"