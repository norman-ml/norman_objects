from typing import Dict, List

from norman_objects.models.http_request_type import HttpRequestType
from norman_objects.models.model_hosting_location import ModelHostingLocation
from norman_objects.models.model_preview import ModelPreview
from norman_objects.models.model_type import ModelType
from norman_objects.models.output_format import OutputFormat
from norman_objects.signatures.model_signature import ModelSignature

class Model(ModelPreview):
    name: str
    url: str
    request_type: HttpRequestType
    model_type: ModelType
    hosting_location: ModelHostingLocation
    output_format: OutputFormat
    long_description: str

    inputs: List[ModelSignature] = []
    outputs: List[ModelSignature] = []
    http_headers: Dict[str, str] = {}
