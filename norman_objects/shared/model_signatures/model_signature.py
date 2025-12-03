from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.model_signatures.http_location import HttpLocation
from norman_objects.shared.model_signatures.receive_format import ReceiveFormat
from norman_objects.shared.model_signatures.signature_transform import SignatureTransform
from norman_objects.shared.model_signatures.signature_type import SignatureType
from norman_objects.shared.parameters.data_modality import DataModality
from norman_objects.shared.parameters.model_param import ModelParam


class ModelSignature(NormanBaseModel):
    id: str = "0"
    model_id: str = "0"
    model_version_id: str = "0"
    signature_type: SignatureType
    data_modality: DataModality
    data_domain: str
    data_encoding: str
    receive_format: ReceiveFormat
    http_location: HttpLocation
    hidden: bool
    display_title: str
    default_value: Optional[str] = None

    parameters: list[ModelParam] = []
    transforms: list[SignatureTransform] = []
    signature_args: dict[str, str] = {}