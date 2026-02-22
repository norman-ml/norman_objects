from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.encoding.channel_encoding import ChannelEncoding
from norman_objects.shared.encoding.sample_encoding import SampleEncoding
from norman_objects.shared.encoding.tensor_encoding import TensorEncoding
from norman_objects.shared.modality.channel_modality import ChannelModality


class ParameterRepresentation(NormanBaseModel):
    channel_modality: ChannelModality
    channel_encoding: ChannelEncoding
    sample_encoding: SampleEncoding
    tensor_encoding: TensorEncoding
