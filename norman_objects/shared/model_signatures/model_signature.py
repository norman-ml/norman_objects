from typing import Optional

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.model_signatures.http_location import HttpLocation
from norman_objects.shared.model_signatures.receive_format import ReceiveFormat
from norman_objects.shared.model_signatures.signature_transform import SignatureTransform
from norman_objects.shared.model_signatures.signature_type import SignatureType
from norman_objects.shared.parameters.data_modality import DataModality
from norman_objects.shared.parameters.model_param import ModelParam


class ModelSignature(NormanBaseModel):
    """
    Defines a structured input or output signature for a model, describing
    the expected modality, encoding, transport format, and associated
    transformation logic.

    Model signatures represent the schema and metadata for either input or
    output elements of a model invocation.

    **Fields**

    - **id** (`str`)
      Unique identifier for this signature. Defaults to `"0"`.

    - **model_id** (`str`)
      Identifier of the model this signature belongs to. Defaults to `"0"`.

    - **signature_type** (`SignatureType`)
      Type of signature:
      - `SignatureType.Input`
      - `SignatureType.Output`

    - **data_modality** (`DataModality`)
      Modality of the data (e.g., `"Text"`, `"Image"`, `"Audio"`).

    - **data_domain** (`str`)
      Domain-specific description of the data (e.g., `"English"`, `"RGB"`).

    - **data_encoding** (`str`)
      Encoding scheme used (e.g., `"utf-8"`, `"base64"`, `"float32"`).

    - **receive_format** (`ReceiveFormat`)
      How data is delivered to or from the model:
      - `ReceiveFormat.File`
      - `ReceiveFormat.Link`
      - `ReceiveFormat.Primitive`

    - **http_location** (`HttpLocation`)
      Location in the HTTP request where this field should appear.

    - **hidden** (`bool`)
      Whether this signature should be hidden from user-facing UIs.

    - **display_title** (`str`)
      Human-friendly label for the signature.

    - **default_value** (`Optional[str]`)
      Default value applied if not provided by the user.

    - **parameters** (`list[ModelParam]`)
      List of additional parameter definitions linked to this signature.

    - **transforms** (`list[SignatureTransform]`)
      Ordered transformations applied before model execution.

    - **signature_args** (`dict[str, str]`)
      Additional arguments or metadata associated with this signature.
    """
    id: str = "0"
    model_id: str = "0"
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
