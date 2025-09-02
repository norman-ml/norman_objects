from norman_objects.messages.entity_type import EntityType
from norman_objects.services.file_push.pairing.socket_pairing_request import SocketPairingRequest


class SocketInputPairingRequest(SocketPairingRequest):
    invocation_id: str
    input_id: str

    @SocketPairingRequest.entity_id.getter
    def entity_id(self):
        return self.input_id

    @SocketPairingRequest.entity_type.getter
    def entity_type(self):
        return EntityType.Input
