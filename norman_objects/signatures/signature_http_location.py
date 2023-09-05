from enum import Enum


class SignatureHttpLocation(str, Enum):
    Body = "Body"
    Path = "Path"
    Query = "Query"