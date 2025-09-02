from norman_objects.shared.messages import EntityType
from norman_objects.services.file_push.pairing.socket_pairing_request import SocketPairingRequest


class SocketAssetPairingRequest(SocketPairingRequest):
    asset_id: str

    @SocketPairingRequest.entity_id.getter
    def entity_id(self):
        return self.asset_id

    @SocketPairingRequest.entity_type.getter
    def entity_type(self):
        return EntityType.Asset
