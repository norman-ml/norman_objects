from enum import StrEnum

class AuthorizationAudiences(StrEnum):
    client = "norman:client"
    quotas = "norman:quotas"
    server = "norman:server"