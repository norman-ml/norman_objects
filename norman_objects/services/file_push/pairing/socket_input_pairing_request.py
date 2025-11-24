from norman_objects.services.file_push.pairing.socket_pairing_request import SocketPairingRequest
from norman_objects.shared.messages.entity_type import EntityType


class SocketInputPairingRequest(SocketPairingRequest):
    """
    Request object used to pair a socket session specifically for model
    input streaming.

    Extends `SocketPairingRequest` with input-specific identifiers.

    **Fields**

    - **account_id** (`str`)
      Inherited from `SocketPairingRequest`.

    - **model_id** (`str`)
      Inherited from `SocketPairingRequest`.

    - **file_size_in_bytes** (`int`)
      Inherited from `SocketPairingRequest`.

    - **invocation_id** (`str`)
      Identifier of the invocation receiving the streamed input.

    - **input_id** (`str`)
      Identifier of the specific input being streamed to the model.
    """
    invocation_id: str
    input_id: str

    @SocketPairingRequest.entity_id.getter
    def entity_id(self):
        return self.input_id

    @SocketPairingRequest.entity_type.getter
    def entity_type(self):
        return EntityType.Input
