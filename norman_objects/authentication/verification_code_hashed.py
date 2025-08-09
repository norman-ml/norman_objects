from dataclasses import dataclass
from datetime import datetime

from norman_objects.norman_objects.authentication.argon2_hash import Argon2Hash


@dataclass
class VerificationCodeHashed(Argon2Hash):
    id: str
    account_id: str
    creation_time: datetime
    expiration_time: datetime
    confirmed: bool
