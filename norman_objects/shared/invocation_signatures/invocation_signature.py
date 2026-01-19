from typing import Annotated

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.hydration.id_markers import GeneratedId, DerivedId


class InvocationSignature(NormanBaseModel):
    id: Annotated[str, GeneratedId()]
    account_id: str
    model_id: str
    version_id: str
    signature_id: str
    invocation_id: Annotated[str, DerivedId("invocation_id")]
    display_title: str = ""
