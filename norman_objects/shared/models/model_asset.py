from norman_objects.norman_base_model import NormanBaseModel


class ModelAsset(NormanBaseModel):
    """
    Represents a stored asset associated with a model version, such as
    a file, artifact, or resource produced or required by the model.

    **Fields**

    - **id** (`str`)
      Unique identifier for the asset. Defaults to `"0"`.

    - **account_id** (`str`)
      Account that owns the asset.

    - **model_id** (`str`)
      Identifier of the model version this asset belongs to.
      Defaults to `"0"`.

    - **asset_name** (`str`)
      Name of the asset (e.g., `"tokenizer.json"`, `"weights.safetensors"`).
    """
    id: str = "0"
    account_id: str
    model_id: str = "0"
    asset_name: str

