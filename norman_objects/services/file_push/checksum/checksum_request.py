from pydantic import BaseModel

class ChecksumRequest(BaseModel):
    account_id: str
    model_id: str
    pairing_id: str
    checksum: str
