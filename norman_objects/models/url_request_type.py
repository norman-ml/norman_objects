from enum import Enum


class UrlRequestType(str, Enum):
    Get = "Get"
    Post = "Post"
    Put = "Put"
