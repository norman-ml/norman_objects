from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.encoding.container_encoding import ContainerEncoding
from norman_objects.shared.modality.container_modality import ContainerModality
from norman_objects.shared.model_signatures.http_location import HttpLocation
from norman_objects.shared.model_signatures.receive_format import ReceiveFormat
from norman_objects.shared.model_signatures.signature_transform import SignatureTransform
from norman_objects.shared.model_signatures.signature_type import SignatureType
from norman_objects.shared.parameters.model_parameter import ModelParameter


class ModelSignature(NormanBaseModel):
    id: str = "0"
    model_id: str = "0"
    version_id: str = "0"
    signature_type: SignatureType
    container_modality: ContainerModality
    data_domain: str
    container_encoding: ContainerEncoding
    receive_format: ReceiveFormat
    http_location: HttpLocation
    hidden: bool
    display_title: str
    default_value: Optional[str] = None

    parameters: list[ModelParameter] = []
    transforms: list[SignatureTransform] = []
    arguments: dict[str, str] = {}
