from norman_objects.norman_base_model import NormanBaseModel


class SignatureTransform(NormanBaseModel):
    """
    Defines a transformation step applied to a signature's data before
    invocation, such as conversion, normalization, or preprocessing.

    **Fields**

    - **id** (`str`)
      Unique identifier for this transform. Defaults to `"0"`.

    - **signature_id** (`str`)
      Identifier of the signature this transform belongs to. Defaults to `"0"`.

    - **transform_name** (`str`)
      Name of the transform operation (e.g., `"resize"`, `"normalize"`).

    - **transform_args** (`dict[str, str]`)
      Key-value arguments used by the transform.
    """
    id: str = "0"
    signature_id: str = "0"
    transform_name: str
    transform_args: dict[str, str] = {}

