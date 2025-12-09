from norman_objects.shared.models.model_preview import ModelPreview
from norman_objects.norman_base_model import NormanBaseModel

class ModelBase(NormanBaseModel):
    """
    Represents the root entity for a model family, containing shared metadata
    across all versions of the model.

    A `ModelBase` groups all model previews (versions) and tracks aggregated
    usage information such as invocation counts.

    **Fields**

    - **id** (`str`)
      Unique identifier for the model base.

    - **account_id** (`str`)
      Account that owns this model.

    - **name** (`str`)
      Human-readable name for the model base (not version-specific).

    - **invocation_count** (`int`)
      Total number of invocations across all model versions.

    - **model_previews** (`list[ModelPreview]`)
      List of model versions (previews) belonging to this base.
      Each element is a `ModelPreview` instance.
    """
    id: str
    account_id: str
    name: str
    invocation_count: int
    model_previews: list[ModelPreview] = []

