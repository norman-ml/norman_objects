from pydantic import BaseModel

from norman_objects.services.file_push.pairing.socket_input_pairing_request import SocketInputPairingRequest


class ChecksumRequest(BaseModel):
    pairing_request: SocketInputPairingRequest
    checksum: str
