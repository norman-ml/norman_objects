from typing_extensions import override

from norman_objects.services.file_pull.file_download_request import NormanFileDownloadRequest
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.messages.output_message import OutputMessage
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue


class OutputDownloadRequest(NormanFileDownloadRequest):
    signature_id: str
    invocation_id: str
    output_id: str

    @NormanFileDownloadRequest.entity_id.getter
    def entity_id(self):
        return self.output_id

    @NormanFileDownloadRequest.entity_type.getter
    def entity_type(self):
        return EntityType.Asset

    @override
    def to_base_message(self, flag_value: StatusFlagValue):
        status_flag = super().to_status_flag(flag_value)
        return OutputMessage.base_message(status_flag)
