from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.accounts.account import Account


class SignupKeyResponse(NormanBaseModel):
    """
    Response returned after a successful API-key-based signup flow.

    Contains the created account and the newly issued API key.

    **Fields**

    - **account** (`Account`)
      The newly created account object.

    - **api_key** (`str`)
      The generated API key associated with the new account.
    """
    account: Account
    api_key: str
