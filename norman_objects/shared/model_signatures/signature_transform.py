from typing import Annotated, Dict

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.hydration.id_markers import GeneratedId, DerivedId


class SignatureTransform(NormanBaseModel):
    id: Annotated[str, GeneratedId()]
    signature_id: Annotated[str, DerivedId("signature_id")]
    transform_name: str
    transform_args: Dict[str, str] = {}
