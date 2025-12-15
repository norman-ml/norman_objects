from pydantic import BaseModel


class SocketPairingResponse(BaseModel):
    pairing_id: str
    host: str
    port: int
    encryption_key: str
    nonce: str
    authentication_header: str
