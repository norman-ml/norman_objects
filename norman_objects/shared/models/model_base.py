from datetime import datetime, timezone

from pydantic import Field, model_validator

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.models.aggregate_tag import AggregateTag


class ModelBase(NormanBaseModel):
    id: str
    account_id: str
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))

    name: str
    category: str
    invocation_count: int

    aggregate_tags: list[AggregateTag] = []

    @model_validator(mode="after")
    def run_validators(self):
        self.validate_model_id()
        return self

    def validate_model_id(self):
        for tag in self.aggregate_tags:
            if self.id != tag.model_id:
                raise ValueError("Model base id does not match aggregate tag model id")
