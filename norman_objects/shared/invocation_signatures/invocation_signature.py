import os

from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.context.norman_path_context import NormanPathContext
from norman_objects.shared.files.partition_name import PartitionName
from norman_objects.shared.messages.entity_type import EntityType
from norman_objects.shared.model_signatures.signature_type import SignatureType


class InvocationSignature(NormanBaseModel):
    id: str = "0"
    account_id: str
    model_id: str
    version_id: str
    signature_id: str
    invocation_id: str = "0"
    signature_type: SignatureType

    def _file_path(self, file_name: str):
        mountpoint = NormanPathContext.get_mountpoint()
        partition_name = PartitionName.Ephemeral.value.lower()
        pluralized_entity_type = f"{EntityType.Invocation.name.lower()}s"
        signature_type = self.signature_type.name.lower()

        path = os.sep.join([
            mountpoint,
            partition_name,
            self.account_id,
            self.model_id,
            self.version_id,
            pluralized_entity_type,
            self.invocation_id,
            signature_type,
            self.id,
            file_name
        ])

        return path

    def staging_path(self):
        return self._file_path(file_name="staged")

    def transcoding_path(self):
        return self._file_path(file_name="transcoded")

    def tensor_path(self, parameter_id: str):
        return self._file_path(file_name=parameter_id)

    def storage_path(self, file_name: str):
        data_bucket_name = NormanPathContext.get_data_bucket()

        bucket = os.sep.join([
            data_bucket_name,
            self.account_id,
            self.model_id,
            self.version_id,
            self.invocation_id,
            self.id,
            file_name
        ])

        return bucket
