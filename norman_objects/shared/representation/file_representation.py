from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.encoding.container_encoding import ContainerEncoding
from norman_objects.shared.modality.container_modality import ContainerModality


class FileRepresentation(NormanBaseModel):
    container_modality: ContainerModality
    container_encoding: ContainerEncoding
    mime_type: str

    def to_metadata(self):
        return {
            "container_modality": self.container_modality,
            "container_encoding": self.container_encoding,
            "mime-type": self.mime_type,  # HTTP relies on a mime-type header for content type resolving.
            "Content-Type": self.mime_type  # S3 relies on Content-Type for proper file handling.
        }
