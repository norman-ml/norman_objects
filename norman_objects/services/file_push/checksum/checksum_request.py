from pydantic import BaseModel


class ChecksumRequest(BaseModel):
    entity_id: str # Used for trace id derivation
    pairing_id: str
    checksum: str
