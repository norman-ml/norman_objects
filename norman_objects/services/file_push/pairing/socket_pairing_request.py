from pydantic import BaseModel


class SocketPairingRequest(BaseModel):
    account_id: str
    model_id: str
    file_size_in_bytes: int

    @property
    def entity_id(self):
        raise NotImplementedError("Pairing request subclasses must return an entity id")

    @property
    def entity_type(self):
        raise NotImplementedError("Pairing request subclasses must return an entity type")

    @property
    def entity_name(self):
        return self.entity_type.name.lower()
