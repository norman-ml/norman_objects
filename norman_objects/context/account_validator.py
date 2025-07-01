from contextlib import ContextDecorator
from norman_objects.context.context_tokens import NormanContext
from norman_objects.exceptions.unauthorized_exception import UnauthorizedException
from norman_utils.cloud.cognito_utils import CognitoUtils


class AccountValidator(ContextDecorator):
    def __init__(self, expected_account_id: str):
        self.__cognito_utils = CognitoUtils()
        self.expected_account_id = expected_account_id

    def __enter__(self):
        decoded_token = NormanContext.decoded_access_token.get(None)
        if decoded_token is not None:
            token_account_id = decoded_token.value().get("cognito:username")
        else:
            access_token = NormanContext.access_token.get(None)
            raw_decoded_token = self.__cognito_utils.decode_jwt_token(access_token)
            token_account_id = raw_decoded_token.get("cognito:username")

        if token_account_id != self.expected_account_id:
            raise UnauthorizedException("Account ID mismatch. Access denied.")

        return self.expected_account_id

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
