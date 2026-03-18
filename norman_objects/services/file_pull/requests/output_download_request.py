from norman_objects.services.file_pull.requests.file_download_request import NormanFileDownloadRequest
from norman_objects.shared.entities.entity_type import EntityType


class OutputDownloadRequest(NormanFileDownloadRequest):
    signature_id: str
    invocation_id: str
    output_id: str

    @NormanFileDownloadRequest.entity_id.getter
    def entity_id(self):
        return self.output_id

    @NormanFileDownloadRequest.entity_type.getter
    def entity_type(self):
        return EntityType.Output
