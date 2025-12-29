from typing import Union, Annotated

from pydantic import Field

from norman_objects.shared.invocation_signatures.invocation_input import InvocationInput
from norman_objects.shared.invocation_signatures.invocation_output import InvocationOutput

InvocationSignatureUnion = Annotated[
    Union[
        InvocationInput,
        InvocationOutput
    ],
    Field(discriminator="signature_type")
]
