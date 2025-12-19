from datetime import datetime, timezone
from typing import Optional

from pydantic import Field

from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.model_signatures.model_signature import ModelSignature
from norman_objects.shared.models.http_request_type import HttpRequestType
from norman_objects.shared.models.model_asset import ModelAsset
from norman_objects.shared.models.model_build_status import ModelBuildStatus
from norman_objects.shared.models.model_hosting_location import ModelHostingLocation
from norman_objects.shared.models.model_type import ModelType
from norman_objects.shared.models.model_version_preview import ModelVersionPreview
from norman_objects.shared.models.output_format import OutputFormat


class ModelVersion(ModelVersionPreview):
    id: str = "0"
    account_id: str
    model_id: str = "0"
    update_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))

    build_status: ModelBuildStatus
    active: bool = True

    label: str
    short_description: str
    long_description: str

    hosting_location: ModelHostingLocation
    model_type: ModelType
    request_type: HttpRequestType
    url: Optional[str] = None
    output_format: OutputFormat

    assets: list[ModelAsset] = []
    inputs: list[ModelSignature] = []
    outputs: list[ModelSignature] = []
    http_headers: dict[str, str] = {}
