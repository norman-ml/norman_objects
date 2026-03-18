from norman_objects.services.file_pull.requests.file_download_request import NormanFileDownloadRequest
from norman_objects.shared.entities.entity_type import EntityType


class InputDownloadRequest(NormanFileDownloadRequest):
    signature_id: str
    invocation_id: str
    input_id: str

    @NormanFileDownloadRequest.entity_id.getter
    def entity_id(self):
        return self.input_id

    @NormanFileDownloadRequest.entity_type.getter
    def entity_type(self):
        return EntityType.Input
