from pydantic import model_validator

from norman_objects.shared.models.http_request_type import HttpRequestType
from norman_objects.shared.models.model_hosting_location import ModelHostingLocation
from norman_objects.shared.models.model_preview import ModelPreview
from norman_objects.shared.models.model_type import ModelType
from norman_objects.shared.models.output_format import OutputFormat
from norman_objects.shared.model_signatures.model_signature import ModelSignature

class Model(ModelPreview):
    name: str
    url: str = ""
    request_type: HttpRequestType = HttpRequestType.Post
    model_type: ModelType = ModelType.Pytorch_jit
    hosting_location: ModelHostingLocation = ModelHostingLocation.Internal
    output_format: OutputFormat = OutputFormat.Json
    long_description: str

    inputs: list[ModelSignature] = []
    outputs: list[ModelSignature] = []
    http_headers: dict[str, str] = {}

    @model_validator(mode="after")
    def validate_url(self) -> "Model":
        if self.hosting_location == ModelHostingLocation.External and self.url == "":
                raise ValueError("url must be provided for external model")
        return self
