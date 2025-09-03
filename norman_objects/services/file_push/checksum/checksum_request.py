from pydantic import BaseModel

class ChecksumRequest(BaseModel):
    pairing_id: str
    checksum: str
