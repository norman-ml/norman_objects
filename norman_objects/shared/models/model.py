from datetime import datetime, timezone

from pydantic import Field, model_validator

from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.models.aggregate_tag import AggregateTag
from norman_objects.shared.models.model_preview import ModelPreview
from norman_objects.shared.models.model_tag import ModelTag
from norman_objects.shared.models.model_version import ModelVersion


class Model(ModelPreview):
    id: str = "0"
    account_id: str
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))

    name: str
    category: str
    invocation_count: int

    versions: list[ModelVersion] = []
    aggregate_tags: list[AggregateTag] = []
    user_tags: list[ModelTag] = []

    @model_validator(mode="after")
    def run_validators(self):
        self.validate_account_id()
        self.validate_model_id()
        return self

    def validate_account_id(self):
        super().validate_account_id()

        for tag in self.user_tags:
            if self.account_id != tag.account_id:
                raise ValueError("Model account id does not match user tag account id")

    def validate_model_id(self):
        super().validate_model_id()

        for tag in self.user_tags:
            if self.id != tag.model_id:
                raise ValueError("Model id does not match user tag model id")
