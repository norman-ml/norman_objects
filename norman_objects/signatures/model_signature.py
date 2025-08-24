from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.parameters.data_domain import DataDomain
from norman_objects.parameters.model_param import ModelParam
from norman_objects.signatures.http_location import HttpLocation
from norman_objects.signatures.receive_format import ReceiveFormat
from norman_objects.signatures.signature_transform import SignatureTransform
from norman_objects.signatures.signature_type import SignatureType


class ModelSignature(NormanBaseModel):
    id: str = "0"
    model_id: str = "0"
    signature_type: SignatureType
    data_domain: DataDomain
    data_encoding: str
    receive_format: ReceiveFormat
    http_location: HttpLocation
    hidden: bool
    display_title: str
    default_value: Optional[str] = None

    parameters: list[ModelParam] = []
    transforms: list[SignatureTransform] = []
    signature_args: dict[str, str] = {}