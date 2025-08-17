from norman_objects.authentication.algorithm_enum import AlgorithmEnum
from norman_objects.norman_base_model import NormanBaseModel


class CredentialHash(NormanBaseModel):
    id: str = "0"
    salt: bytes
    hash: bytes
    time_cost: int
    memory_cost: int
    parallelism: int
    hash_length: int
    algorithm: AlgorithmEnum
    version: int
