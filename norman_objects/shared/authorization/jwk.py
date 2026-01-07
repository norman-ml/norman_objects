from norman_objects.norman_base_model import NormanBaseModel


class Jwk(NormanBaseModel):
    kty: str
    kid: str
    use: str
    alg: str
    n: str
    e: str
