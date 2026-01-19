from typing import Annotated, Dict, List, Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.model_signatures.http_location import HttpLocation
from norman_objects.shared.model_signatures.receive_format import ReceiveFormat
from norman_objects.shared.model_signatures.signature_transform import SignatureTransform
from norman_objects.shared.model_signatures.signature_type import SignatureType
from norman_objects.shared.parameters.data_modality import DataModality
from norman_objects.shared.parameters.model_param import ModelParam
from norman_objects.hydration.id_markers import GeneratedId, DerivedId


class ModelSignature(NormanBaseModel):
    id: Annotated[str, GeneratedId(context_key="signature_id")]
    model_id: Annotated[str, DerivedId("model_id")]
    version_id: Annotated[str, DerivedId("version_id")]
    signature_type: SignatureType
    data_modality: DataModality
    data_domain: str
    data_encoding: str
    receive_format: ReceiveFormat
    http_location: HttpLocation
    hidden: bool
    display_title: str
    default_value: Optional[str] = None

    parameters: List[ModelParam] = []
    transforms: List[SignatureTransform] = []
    signature_args: Dict[str, str] = {}