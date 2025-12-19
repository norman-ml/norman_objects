from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.services.file_pull.requests.file_download_request import NormanFileDownloadRequest
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.messages.model_message import ModelMessage
from norman_objects.shared.models.model_projection import ModelProjection
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class TrackedDownload(NormanBaseModel):
    download_request: NormanFileDownloadRequest
    file_link: str
    model: ModelProjection
    entity_type: EntityType

    downloaded_bytes: int = 0
    total_bytes: int = 0
    file_checksum: str = ""

    @property
    def entity_id(self):
        raise NotImplementedError("Tracked download config subclasses must return an entity id")

    @property
    def entity_type(self):
        raise NotImplementedError("Tracked download config subclasses must return an entity type")

    @property
    def entity_name(self):
        return self.entity_type.name.lower()

    def to_message(self, flag_value: StatusFlagValue) -> ModelMessage:
        raise NotImplementedError("Download request subclasses must implement this method to serialize to a message")
