from norman_objects.norman_base_model import NormanBaseModel


class ModelTag(NormanBaseModel):
    """
    Represents a tag attached to a specific model version or model base.

    Tags are used for categorization, search, and metadata annotation.

    **Fields**

    - **id** (`str`)
      Unique identifier for the tag record. Defaults to `"0"`.

    - **account_id** (`str`)
      Account that owns the tag. Defaults to `"0"`.

    - **model_id** (`str`)
      Identifier of the model or model version this tag applies to.
      Defaults to `"0"`.

    - **name** (`str`)
      The textual tag value (e.g., `"nlp"`, `"embedding"`, `"beta"`).
    """
    id: str = "0"
    account_id: str = "0"
    model_id: str = "0"
    name: str

