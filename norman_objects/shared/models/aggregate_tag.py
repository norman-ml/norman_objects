from norman_objects.norman_base_model import NormanBaseModel


class AggregateTag(NormanBaseModel):
    """
    Represents an aggregated tag associated with a model, tracking the number
    of times this tag appears across all model versions or entities.

    **Fields**

    - **model_id** (`str`)
      Identifier of the model to which this aggregated tag applies.

    - **name** (`str`)
      Tag label (e.g., `"nlp"`, `"vision"`, `"beta"`).

    - **tag_count** (`int`)
      Number of occurrences of this tag across all relevant entities
      (versions, previews, metadata, etc.).
    """
    model_id: str
    name: str
    tag_count: int
