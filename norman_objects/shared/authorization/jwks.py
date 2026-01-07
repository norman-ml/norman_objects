from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.authorization.jwk import Jwk


class Jwks(NormanBaseModel):
    key_set: list[Jwk]
