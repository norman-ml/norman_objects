from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.encoding.container_encoding import ContainerEncoding
from norman_objects.shared.modality.container_modality import ContainerModality


class SignatureRepresentation(NormanBaseModel):
    container_modality: ContainerModality
    container_encoding: ContainerEncoding
