from datetime import datetime, timezone
from typing import Annotated, Dict, List, Optional

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
from norman_objects.hydration import GeneratedId, DerivedId


class ModelVersion(ModelVersionPreview):
    # ID is generated and exposed as "version_id" in context for children
    id: Annotated[str, GeneratedId(context_key="version_id")]
    account_id: str = ""
    model_id: Annotated[str, DerivedId("model_id")]
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

    assets: List[ModelAsset] = []
    inputs: List[ModelSignature] = []
    outputs: List[ModelSignature] = []
    http_headers: Dict[str, str] = {}
