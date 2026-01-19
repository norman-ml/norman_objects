from datetime import datetime, timezone
from typing import Annotated

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.invocation_signatures.invocation_signature import InvocationSignature
from norman_objects.hydration.id_markers import GeneratedId


class Invocation(NormanBaseModel):
    id: Annotated[str, GeneratedId(context_key="invocation_id")]
    account_id: str
    model_id: str
    version_id: str
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))

    inputs: list[InvocationSignature] = []
    outputs: list[InvocationSignature] = []
