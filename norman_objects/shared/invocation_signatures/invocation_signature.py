from norman_objects.norman_base_model import NormanBaseModel


class InvocationSignature(NormanBaseModel):
    """
    Represents a single input signature associated with an invocation.

    An `InvocationSignature` links an invocation to one of its signature
    definitions (e.g., an input schema). It is used
    to describe the structure, labeling, and ownership of each element
    that participated in the invocation.

    **Fields**

    - **id** (`str`)
      Unique identifier for this signature instance. Defaults to `"0"`.

    - **account_id** (`str`)
      Identifier of the account that owns this signature.

    - **model_id** (`str`)
      Identifier of the model associated with this signature.

    - **signature_id** (`str`)
      Identifier of the signature template or schema being referenced.

    - **invocation_id** (`str`)
      Identifier of the invocation this signature belongs to.
      Defaults to `"0"`.

    - **display_title** (`str`)
      Human-readable title used for UI labeling and presentation.
      Defaults to an empty string.
    """
    id: str = "0"
    account_id: str
    model_id: str
    signature_id: str
    invocation_id: str = "0"
    display_title: str = ""
