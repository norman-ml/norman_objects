from datetime import datetime, timezone
from typing import Optional

from pydantic import Field

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.date.normalized_datetime import NormalizedDateTime
from norman_objects.shared.models.aggregate_tag import AggregateTag
from norman_objects.shared.models.model_asset import ModelAsset
from norman_objects.shared.models.model_build_status import ModelBuildStatus


class ModelPreview(NormanBaseModel):
    """
    Represents a specific version of a model, including metadata, assets,
    and descriptive information.

    Model previews are versioned instances under a `ModelBase`, each with
    its own version label, description, and activation status.

    **Fields**

    - **id** (`str`)
      Unique identifier for this model preview. Defaults to `"0"`.

    - **account_id** (`str`)
      Account that owns this model version.

    - **model_base_id** (`str`)
      Identifier of the parent `ModelBase`. Defaults to `"0"`.

    - **version_label** (`str`)
      Version name or tag.

    - **active** (`bool`)
      Whether this version is currently active. Defaults to `True`.

    - **creation_time** (`datetime`)
      UTC timestamp when this version was created.
      Defaults to the current UTC time.

    - **short_description** (`str`)
      Human-readable summary describing this model version.

    - **assets** (`list[ModelAsset]`)
      List of assets associated with this model preview.

    - **tags** (`list[AggregateTag]`)
      List of tags aggregated at this version level.
    """
    id: str = "0"
    account_id: str
    model_base_id: str = "0"
    version_label: str
    active: bool = True
    build_status: Optional[ModelBuildStatus] = None
    creation_time: NormalizedDateTime = Field(default_factory=lambda: datetime.now(timezone.utc))
    short_description: str

    assets: list[M]()

