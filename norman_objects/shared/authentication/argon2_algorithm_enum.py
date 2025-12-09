from enum import Enum

class Argon2AlgorithmEnum(str, Enum):
    """
    Enumeration of Argon2 hashing algorithm variants supported by the system.

    **Values**

    - **ID** — Argon2id (combined defense against GPU and side-channel attacks)
    - **I** — Argon2i (optimized for password hashing)
    - **D** — Argon2d (optimized for fast hashing, less side-channel resistant)
    """
    ID = "ID"
    I = "I"
    D = "D"
