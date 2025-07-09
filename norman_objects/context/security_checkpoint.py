from typing import Iterable

from fastapi import HTTPException
from norman_objects.context.context_tokens import NormanContext
from starlette import status


class SecurityCheckpoint:
    def __init__(self, required_scopes: [str]):
        self.required_scopes = required_scopes

    def __enter__(self):
        token_account_id = self.security_checks()
        return token_account_id

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def security_checks(self):
        decoded_token = NormanContext.decoded_access_token.get(None)
        if decoded_token is None or not isinstance(decoded_token.value(), dict):
            raise ValueError("Cannot validate account without a proper access token")


        claims = decoded_token.value()

        # raw_scopes = claims.get("scope") or claims.get("scopes")
        # if raw_scopes is None:
        #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token contains no scope claim")
        #
        # if isinstance(raw_scopes, str):
        #     token_scopes = raw_scopes.split()
        # elif isinstance(raw_scopes, Iterable):
        #     token_scopes = list(raw_scopes)
        # else:
        #     token_scopes = []
        #
        # missing = [scope for scope in self.required_scopes if scope not in token_scopes]
        # if len(missing) > 0:
        #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Missing required scopes: {', '.join(missing)}")

        token_account_id = decoded_token.value().get("cognito:username")
        return token_account_id
