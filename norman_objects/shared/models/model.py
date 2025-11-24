from norman_objects.shared.model_signatures.model_signature import ModelSignature
from norman_objects.shared.models.http_request_type import HttpRequestType
from norman_objects.shared.models.model_hosting_location import ModelHostingLocation
from norman_objects.shared.models.model_preview import ModelPreview
from norman_objects.shared.models.model_tag import ModelTag
from norman_objects.shared.models.model_type import ModelType
from norman_objects.shared.models.output_format import OutputFormat


class Model(ModelPreview):
    name: str
    model_class: str
    url: str | None = None
    request_type: HttpRequestType | None = None
    model_type: ModelType
    hosting_location: ModelHostingLocation
    output_format: OutputFormat
    long_description: str

    inputs: list[ModelSignature] = []
    outputs: list[ModelSignature] = []
    http_headers: dict[str, str] = {}
    user_added_tags: list[ModelTag] = []
