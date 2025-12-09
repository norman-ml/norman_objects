from norman_objects.shared.authentication.argon2_algorithm_enum import Argon2AlgorithmEnum
from norman_objects.norman_base_model import NormanBaseModel


class CredentialHash(NormanBaseModel):
    """
    Represents a stored hashed credential using Argon2 parameters.

    This object encapsulates all components required to verify a password
    or OTP against its Argon2 hash.

    **Fields**

    - **id** (`str`)
      Unique identifier for the credential hash entry. Defaults to `"0"`.

    - **salt** (`bytes`)
      Random salt applied during hashing.

    - **hash** (`bytes`)
      Raw Argon2 hash output.

    - **time_cost** (`int`)
      Argon2 time cost parameter (number of iterations).

    - **memory_cost** (`int`)
      Memory cost parameter in kibibytes.

    - **parallelism** (`int`)
      Number of parallel threads used during hashing.

    - **hash_length** (`int`)
      Length of the resulting hash in bytes.

    - **algorithm** (`Argon2AlgorithmEnum`)
      Variant of the Argon2 algorithm used (ID, I, or D).

    - **version** (`int`)
      Argon2 version number.
    """
    id: str = "0"
    salt: bytes
    hash: bytes
    time_cost: int
    memory_cost: int
    parallelism: int
    hash_length: int
    algorithm: Argon2AlgorithmEnum
    version: int
