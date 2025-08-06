from norman_objects.norman_base_model import NormanBaseModel


class FileProperties(NormanBaseModel):
    entity_id: str
    file_size_in_bytes: int = 0
    file_checksum: str
