from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.parameters.data_modality import DataModality


class ModelParam(NormanBaseModel):
    """
    Represents an auxiliary parameter belonging to a model signature,
    typically used for describing nested fields or advanced configuration
    options.

    **Fields**

    - **id** (`str`)
      Unique identifier for the parameter. Defaults to `"0"`.

    - **model_id** (`str`)
      Identifier of the parent model. Defaults to `"0"`.

    - **signature_id** (`str`)
      Identifier of the signature this parameter belongs to. Defaults to `"0"`.

    - **data_modality** (`DataModality`)
      Modality of the parameter (Text, Image, Integer, etc.).

    - **data_encoding** (`str`)
      Encoding format for this parameter.

    - **parameter_name** (`str`)
      Name of the parameter as exposed to the client.
    """
    id: str = "0"
    model_id: str = "0"
    signature_id: str = "0"
    data_modality: DataModality
    data_encoding: str
    parameter_name: str

