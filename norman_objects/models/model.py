from datetime import datetime, timedelta, timezone
from typing import Dict, List

from pydantic import BaseModel, Field

from norman_objects.models.model_asset import ModelAsset
from norman_objects.models.model_hosting_location import ModelHostingLocation
from norman_objects.models.model_type import ModelType
from norman_objects.models.output_format import OutputFormat
from norman_objects.models.http_request_type import HttpRequestType
from norman_objects.signatures.model_signature import ModelSignature


class Model(BaseModel):
    id: str = "0"
    creation_time: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(0))))
    name: str
    url: str
    request_type: HttpRequestType
    model_type: ModelType
    hosting_location: ModelHostingLocation
    output_format: OutputFormat
    short_description: str
    long_description: str

    inputs: List[ModelSignature] = []
    outputs: List[ModelSignature] = []
    http_headers: Dict[str, str] = {}
    assets: List[ModelAsset] = []
