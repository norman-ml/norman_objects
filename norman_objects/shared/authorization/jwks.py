from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.authorization.jwk import JWK


class JWKS(NormanBaseModel):
    key_set: list[JWK]
