from datetime import datetime, timezone

from pydantic import Field, model_validator

from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.models.model_base import ModelBase
from norman_objects.shared.tags.aggregate_tag import AggregateTag
from norman_objects.shared.versions.model_version_preview import ModelVersionPreview


class ModelPreview(ModelBase):
    id: str
    account_id: str
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))

    name: str
    category: str
    invocation_count: int

    versions: list[ModelVersionPreview] = []
    aggregate_tags: list[AggregateTag] = []

    @model_validator(mode="after")
    def run_validators(self):
        self.validate_account_id()
        self.validate_model_id()
        return self

    def validate_account_id(self):
        for model_version in self.versions:
            if self.account_id != model_version.account_id:
                raise ValueError("Model preview account id does not match model version account id")

    def validate_model_id(self):
        super().validate_model_id()

        for model_version in self.versions:
            if self.id != model_version.model_id:
                raise ValueError("Model preview id does not match model version model id")
