from typing import Literal

from norman_objects.shared.invocation_signatures.invocation_signature import InvocationSignature
from norman_objects.shared.model_signatures.signature_type import SignatureType


class InvocationOutput(InvocationSignature):
    signature_type: Literal[SignatureType.Output] = SignatureType.Output
