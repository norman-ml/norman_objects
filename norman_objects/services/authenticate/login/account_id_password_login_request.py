from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.security.sensitive import Sensitive


class AccountIDPasswordLoginRequest(NormanBaseModel):
    """
    Authentication request using an account ID and password.

    This request is typically used for internal or system-level logins
    where the account ID is already known.

    **Fields**

    - **account_id** (`str`)
      Identifier of the account attempting to authenticate.

    - **password** (`Sensitive[str]`)
      Password wrapped in a `Sensitive` container to ensure safe handling
      in logs, traces, and internal memory.
    """
    account_id: str
    password: Sensitive[str]
