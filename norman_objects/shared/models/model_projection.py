from datetime import datetime, timezone
from typing import Annotated, List

from pydantic import Field

from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.models.aggregate_tag import AggregateTag
from norman_objects.shared.models.model_base import ModelBase
from norman_objects.shared.models.model_tag import ModelTag
from norman_objects.shared.models.model_version import ModelVersion
from norman_objects.hydration import GeneratedId


class ModelProjection(ModelBase):
    # ID is generated and exposed as "model_id" in context for children
    id: Annotated[str, GeneratedId(context_key="model_id")]
    # account_id is provided by client, not derived - stays in CreateSchema
    account_id: str
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))

    name: str
    category: str
    invocation_count: int

    version: ModelVersion
    aggregate_tags: List[AggregateTag] = []
    user_tags: List[ModelTag] = []
