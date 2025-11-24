from pydantic import BaseModel

class SocketPairingResponse(BaseModel):
    """
    Response object returned when establishing a secure socket pairing
    between the client and the Norman platform.

    This pairing provides the necessary session details for encrypted
    real-time communication, such as model input streaming or asset
    transfers.

    **Fields**

    - **pairing_id** (`str`)
      Unique identifier representing this pairing session.

    - **host** (`str`)
      Hostname or IP address of the socket server.

    - **port** (`int`)
      Port number for the socket connection.

    - **encryption_key** (`str`)
      Symmetric encryption key used for securing the socket session.

    - **nonce** (`str`)
      Cryptographic nonce used for message authentication or encryption
      initialization.

    - **authentication_header** (`str`)
      Pre-computed authentication header required for connecting to the
      socket service.
    """
    pairing_id: str
    host: str
    port: int
    encryption_key: str
    nonce: str
    authentication_header: str
