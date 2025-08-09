from dataclasses import dataclass

@dataclass
class Argon2Hash:
    salt: bytes
    hash: bytes
    time_cost: int
    memory_cost: int
    parallelism: int
    hash_length: int
    algorithm: str
    version: int
