from enum import Enum


class RequestMethod(str, Enum):
    Get = "GET"
    Post = "POST"
    Put = "PUT"
    Delete = "DELETE"
