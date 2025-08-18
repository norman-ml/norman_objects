from norman_objects.authentication.argon2_algorithm_enum import Argon2AlgorithmEnum
from norman_objects.norman_base_model import NormanBaseModel


class CredentialHash(NormanBaseModel):
    id: str = "0"
    salt: bytes
    hash: bytes
    time_cost: int
    memory_cost: int
    parallelism: int
    hash_length: int
    algorithm: Argon2AlgorithmEnum
    version: int
