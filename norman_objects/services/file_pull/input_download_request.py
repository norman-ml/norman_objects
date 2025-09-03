from typing_extensions import override

from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.messages.input_message import InputMessage
from norman_objects.shared.status_flags.status_flag_value import StatusFlagValue

from src.objects.requests.file_download_request import NormanFileDownloadRequest


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

    @override
    def to_base_message(self, flag_value: StatusFlagValue):
        status_flag = super().to_status_flag(flag_value)
        return InputMessage.base_message(status_flag)
