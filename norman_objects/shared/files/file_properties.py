from norman_objects.norman_base_model import NormanBaseModel


class FileProperties(NormanBaseModel):
    """
    Represents metadata describing a file associated with an entity,
    typically used for uploads, stored assets, staging, or input files.

    **Fields**

    - **entity_id** (`str`)
      Identifier of the entity associated with this file (e.g., model ID,
      input ID, invocation ID, or asset group).

    - **file_size_in_bytes** (`int`)
      Size of the file in bytes. Defaults to `0` when not yet determined.

    - **file_checksum** (`str`)
      Hash checksum of the file (e.g., SHA256, MD5), used for validation,
      deduplication, or integrity checking.
    """
    entity_id: str
    file_size_in_bytes: int = 0
    file_checksum: str
