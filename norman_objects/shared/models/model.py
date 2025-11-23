from norman_objects.shared.model_signatures.model_signature import ModelSignature
from norman_objects.shared.models.http_request_type import HttpRequestType
from norman_objects.shared.models.model_hosting_location import ModelHostingLocation
from norman_objects.shared.models.model_preview import ModelPreview
from norman_objects.shared.models.model_tag import ModelTag
from norman_objects.shared.models.model_type import ModelType
from norman_objects.shared.models.output_format import OutputFormat
from typing import Optional


class Model(ModelPreview):
    """
    Represents a fully resolved model version, including all execution
    metadata, signature definitions, HTTP configuration, and extended
    descriptive fields.

    A `Model` extends `ModelPreview` with runtime-specific configuration
    such as request types, hosting details, HTTP headers, signature
    structures, and additional user-defined tags.

    **Fields**

    - **name** (`str`)
      Display name for this specific model version.

    - **model_class** (`str`)
      Internal or system-level classification for this model.

    - **url** (`str`)
      Endpoint URL used to invoke the model.

    - **request_type** (`HttpRequestType`)
      HTTP method or request style used to communicate with the model.

    - **model_type** (`ModelType`)
      High-level categorization of the model (e.g., LLM, Embedding, Vision).

    - **hosting_location** (`ModelHostingLocation`)
      Where the model is hosted (e.g., cloud region, local cluster).

    - **output_format** (`OutputFormat`)
      Expected response format or media type.

    - **long_description** (`str`)
      Detailed explanation of model behavior, usage, and capabilities.

    - **inputs** (`list[ModelSignature]`)
      Signature definitions describing all expected input structures.

    - **outputs** (`list[ModelSignature]`)
      Signature definitions describing model output structures.

    - **http_headers** (`dict[str, str]`)
      Additional HTTP headers to attach to requests.

    - **user_added_tags** (`list[ModelTag]`)
      Tags manually added by users for organization or categorization.
    """
    name: str
    model_class: str
    url: Optional[str] = None
    request_type: HttpRequestType
    model_type: ModelType
    hosting_location: ModelHostingLocation
    output_format: OutputFormat
    long_description: str

    inputs: list[ModelSignature] = []
    outputs: list[ModelSignature] = []
    http_headers: dict[str, str] = {}
    user_added_tags: list[ModelTag] = []

