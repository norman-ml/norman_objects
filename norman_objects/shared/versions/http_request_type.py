from enum import Enum


class HttpRequestType(str, Enum):
    Get = "Get"
    Post = "Post"
    Put = "Put"
