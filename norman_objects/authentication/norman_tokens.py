from fastapi import HTTPException
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.sensitive.sensitive_type import SensitiveType


class NormanTokens(NormanBaseModel):
    access_token: SensitiveType(str) = None
    id_token: SensitiveType(str) = None
    refresh_token: SensitiveType(str) = None

