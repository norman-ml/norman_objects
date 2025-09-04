from norman_objects.services.file_pull.requests.file_download_request import NormanFileDownloadRequest
from norman_objects.shared.messages.model_message import ModelMessage
from norman_objects.shared.models.model import Model
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class TrackedDownload:
    def __init__(self, download_request: NormanFileDownloadRequest, file_link: str, model: Model):
        self.download_request = download_request
        self.file_link = file_link
        self.model = model

        self.downloaded_bytes = 0
        self.total_bytes = 0
        self.file_checksum = ""

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
