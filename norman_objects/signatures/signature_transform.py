from typing import Dict

from norman_objects.norman_base_model import NormanBaseModel


class SignatureTransform(NormanBaseModel):
    id: str = "0"
    signature_id: str = "0"
    transform_name: str
    transform_args: Dict[str, str] = {}
