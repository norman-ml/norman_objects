from typing import Dict, List

from pydantic import BaseModel

from norman_objects.models.model_asset import ModelAsset
from norman_objects.models.model_hosting_location import ModelHostingLocation
from norman_objects.models.model_type import ModelType
from norman_objects.models.url_request_type import UrlRequestType
from norman_objects.signatures.model_signature import ModelSignature


class Model(BaseModel):
    id: str = "0"
    name: str
    url: str
    url_request_type: UrlRequestType
    model_type: ModelType
    model_hosting_location: ModelHostingLocation
    short_description: str
    long_description: str

    inputs: List[ModelSignature] = []
    outputs: List[ModelSignature] = []
    http_headers: Dict[str, str] = {}
    assets: List[ModelAsset] = []
