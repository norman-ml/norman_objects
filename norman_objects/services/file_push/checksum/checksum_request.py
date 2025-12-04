from pydantic import BaseModel

class ChecksumRequest(BaseModel):
    """
    Request object used to submit a checksum for a completed socket-based
    file or stream transfer. This is typically sent after an upload or
    streaming session finishes to validate data integrity.

    **Fields**

    - **pairing_id** (`str`)
      Identifier of the socket pairing session associated with the
      transferred file or stream.

    - **checksum** (`str`)
      Hash checksum of the transferred data (e.g., SHA256, MD5).
      Used by the server to verify that the received content matches
      the expected integrity signature.
    """
    pairing_id: str
    checksum: str
