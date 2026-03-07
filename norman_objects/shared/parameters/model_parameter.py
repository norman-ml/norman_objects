from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.encoding.channel_encoding import ChannelEncoding
from norman_objects.shared.encoding.sample_encoding import SampleEncoding
from norman_objects.shared.encoding.tensor_encoding import TensorEncoding
from norman_objects.shared.modality.channel_modality import ChannelModality


class ModelParameter(NormanBaseModel):
    id: str = "0"
    model_id: str = "0"
    version_id: str = "0"
    signature_id: str = "0"
    channel_modality: ChannelModality
    channel_encoding: ChannelEncoding
    sample_encoding: SampleEncoding
    tensor_encoding: TensorEncoding
    name: str

    arguments: dict[str, str] = {}
