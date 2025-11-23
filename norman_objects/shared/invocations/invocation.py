from datetime import datetime, timezone

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.invocation_signatures.invocation_signature import InvocationSignature


class Invocation(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))

    inputs: list[InvocationSignature] = []
    outputs: list[InvocationSignature] = []
