from typing import Dict, List
from pydantic import BaseModel

from norman_objects.models.model_hosting_location import ModelHostingLocation
from norman_objects.models.model_type import ModelType
from norman_objects.models.url_request_type import UrlRequestType
from norman_objects.parameters.model_param import ModelParam


class Model(BaseModel):
    id: str = "0"
    name: str
    url: str
    logo_url: str
    url_request_type: UrlRequestType
    model_type: ModelType
    model_hosting_location: ModelHostingLocation
    short_description: str
    long_description: str

    inputs: List[ModelParam] = []
    outputs: List[ModelParam] = []
    http_headers: Dict[str, str] = {}
