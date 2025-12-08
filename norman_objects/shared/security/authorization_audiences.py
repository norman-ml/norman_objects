from enum import StrEnum

class Audiences(StrEnum):
    client = "norman:client"
    quotas = "norman:quotas"
    server = "norman:server"