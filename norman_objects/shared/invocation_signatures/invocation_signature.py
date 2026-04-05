from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.model_signatures.signature_type import SignatureType


class InvocationSignature(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    version_id: str
    signature_id: str
    invocation_id: str = "0"
    display_title: str = ""
    signature_type: SignatureType
