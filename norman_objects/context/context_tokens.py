from contextvars import ContextVar

from norman_objects.authorization.access_token import AccessToken


class NormanContext:
    _access_token: ContextVar[AccessToken] = ContextVar("norman_access_token")

    @staticmethod
    def get_access_token():
        return NormanContext._access_token.get()

    @staticmethod
    def set_access_token(access_token_dict: dict):
        access_token = AccessToken(
            header=access_token_dict["header"],
            payload=access_token_dict["payload"],
            signature=access_token_dict["signature"]
        )
        NormanContext._access_token.set(access_token)

    @staticmethod
    def clear():
        NormanContext._access_token.set(None)
