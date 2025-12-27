from datetime import datetime, timezone

from pydantic import Field

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
