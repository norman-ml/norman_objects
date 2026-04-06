from datetime import datetime, timezone
from typing import Optional

from pydantic import Field, model_validator

from norman_objects.shared.assets.model_asset import ModelAsset
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.model_signatures.model_signature import ModelSignature
from norman_objects.shared.models.model_build_status import ModelBuildStatus
from norman_objects.shared.versions.http_request_type import HttpRequestType
from norman_objects.shared.versions.model_hosting_location import ModelHostingLocation
from norman_objects.shared.versions.model_type import ModelType
from norman_objects.shared.versions.model_version_preview import ModelVersionPreview
from norman_objects.shared.versions.output_format import OutputFormat


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

    dedicated_provisioning: bool = False
    machine_type: Optional[str] = None
    capacity: int = 0

    assets: list[ModelAsset] = []
    inputs: list[ModelSignature] = []
    outputs: list[ModelSignature] = []
    http_headers: dict[str, str] = {}

    @model_validator(mode="after")
    def run_validators(self):
        self.validate_account_id()
        self.validate_model_id()
        self.validate_version_id()
        self.validate_capacity()
        return self

    def validate_account_id(self):
        super().validate_account_id()

        for input_signature in self.inputs:
            if self.account_id != input_signature.account_id:
                raise ValueError("Model version account id does not match input signature account id")

        for output_signature in self.outputs:
            if self.account_id != output_signature.account_id:
                raise ValueError("Model version account id does not match output signature account id")

    def validate_model_id(self):
        super().validate_model_id()

        for input_signature in self.inputs:
            if self.model_id != input_signature.model_id:
                raise ValueError("Model version model id does not match input signature model id")

        for output_signature in self.outputs:
            if self.model_id != output_signature.model_id:
                raise ValueError("Model version model id does not match output signature model id")

    def validate_version_id(self):
        super().validate_version_id()

        for input_signature in self.inputs:
            if self.id != input_signature.version_id:
                raise ValueError("Model version id does not match input signature version id")

        for output_signature in self.outputs:
            if self.id != output_signature.version_id:
                raise ValueError("Model version id does not match output signature version id")

    def validate_capacity(self):
        if self.capacity < 0:
            raise ValueError("Model version capacity cannot be negative")
