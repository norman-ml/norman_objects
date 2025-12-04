from norman_objects.services.file_push.pairing.socket_pairing_request import SocketPairingRequest
from norman_objects.shared.messages.entity_type import EntityType


class SocketAssetPairingRequest(SocketPairingRequest):
    """
    Request object used to establish a socket pairing session for the
    transfer of model assets (e.g., output artifacts, large intermediary
    files, or staged resources).

    **Fields**

    - **account_id** (`str`)
      Inherited from `SocketPairingRequest`.

    - **model_id** (`str`)
      Inherited from `SocketPairingRequest`.

    - **file_size_in_bytes** (`int`)
      Inherited from `SocketPairingRequest`.

    - **asset_id** (`str`)
      Identifier of the asset being transferred over the socket session.
    """
    asset_id: str

    @SocketPairingRequest.entity_id.getter
    def entity_id(self):
        return self.asset_id

    @SocketPairingRequest.entity_type.getter
    def entity_type(self):
        return EntityType.Asset
