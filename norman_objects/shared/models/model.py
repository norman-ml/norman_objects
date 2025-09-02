from norman_objects.shared.models.http_request_type import HttpRequestType
from norman_objects.shared.models.model_hosting_location import ModelHostingLocation
from norman_objects.shared.models.model_preview import ModelPreview
from norman_objects.shared.models.model_type import ModelType
from norman_objects.shared.models.output_format import OutputFormat
from norman_objects.shared.signatures.model_signature import ModelSignature

class Model(ModelPreview):
    name: str
    url: str
    request_type: HttpRequestType
    model_type: ModelType
    hosting_location: ModelHostingLocation
    output_format: OutputFormat
    long_description: str

    inputs: list[ModelSignature] = []
    outputs: list[ModelSignature] = []
    http_headers: dict[str, str] = {}
