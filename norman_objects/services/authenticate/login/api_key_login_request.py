from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.security.sensitive import Sensitive


class ApiKeyLoginRequest(NormanBaseModel):
    """
    Authentication request using an API key.

    This request type is used for programmatic or machine-to-machine
    authentication flows.

    **Fields**

    - **api_key** (`Sensitive[str]`)
      API key provided by the client. Stored inside `Sensitive` to avoid
      accidental exposure.
    """
    api_key: Sensitive[str]
