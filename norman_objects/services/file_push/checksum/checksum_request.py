from pydantic import BaseModel


class ChecksumRequest(BaseModel):
    pairing_id: str
    checksum: str
    entity_id: str # Used for trace id derivation
