from typing import Dict, List

from pydantic import BaseModel

from norman_objects.parameters.model_param import ModelParam
from norman_objects.parameters.param_domain import ParamDomain
from norman_objects.parameters.param_receive_format import ParamReceiveFormat
from norman_objects.signatures.signature_http_location import SignatureHttpLocation
from norman_objects.signatures.signature_transform import SignatureTransform
from norman_objects.signatures.signature_type import SignatureType


class ModelSignature(BaseModel):
    id: str = "0"
    model_id: str = "0"
    signature_type: SignatureType
    signature_domain: ParamDomain
    mime_type: str
    mime_subtype: str
    receive_format: ParamReceiveFormat
    http_location: SignatureHttpLocation
    display_title: str

    parameters: List[ModelParam] = []
    transforms: List[SignatureTransform] = []
    signature_args: Dict[str, str] = {}