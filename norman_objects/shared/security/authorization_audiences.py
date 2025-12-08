from enum import StrEnum

class AuthorizationAudiences(StrEnum):
    Client = "norman:client"
    Quotas = "norman:quotas"
    Server = "norman:server"