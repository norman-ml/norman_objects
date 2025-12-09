from enum import Enum

class AuthorizationAudiences(str, Enum):
    Client = "norman:client"
    Quotas = "norman:quotas"
    Server = "norman:server"