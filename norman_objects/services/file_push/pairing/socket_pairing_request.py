from pydantic import BaseModel


class SocketPairingRequest(BaseModel):
    """
    Base request object for initiating a socket pairing session.

    This request is used to establish a secure communication channel for
    streaming inputs, uploading large files, or transferring staged assets.

    **Fields**

    - **account_id** (`str`)
      Identifier of the account initiating the socket session.

    - **model_id** (`str`)
      Identifier of the model associated with this pairing.

    - **file_size_in_bytes** (`int`)
      Size of the file or stream (in bytes) expected to be transferred
      through the socket session.
    """
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
