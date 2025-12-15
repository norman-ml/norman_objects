from pydantic import BaseModel

from norman_objects.services.file_push.pairing.socket_pairing_request import SocketPairingRequest


class ChecksumRequest(BaseModel):
    pairing_request: SocketPairingRequest
    pairing_id: str
    checksum: str
