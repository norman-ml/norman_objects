from pydantic import Field

def Sensitive():
    return Field(..., sensitive=True)
