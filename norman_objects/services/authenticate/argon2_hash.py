from norman_objects.norman_base_model import NormanBaseModel


class Argon2Hash(NormanBaseModel):
    id: str = "0"

    salt: bytes
    hash: bytes
    time_cost: int
    memory_cost: int
    parallelism: int
    hash_length: int
    algorithm: str
    version: int
