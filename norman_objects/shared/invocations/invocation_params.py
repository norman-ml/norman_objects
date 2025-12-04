from norman_objects.shared.invocations.invocation import Invocation
from norman_objects.shared.models.model import Model
from norman_objects.norman_base_model import NormanBaseModel
from norman_objects.shared.security.sensitive import Sensitive


class InvocationParams(NormanBaseModel):
    """
    Container object that bundles all parameters required to execute a
    model invocation, including authentication, model metadata, and
    invocation structure.

    This object is typically passed to execution engines, runners, or
    dispatchers responsible for performing the actual model call.

    **Fields**

    - **access_token** (`Sensitive[str]`)
      Bearer token used for authentication during model invocation.

    - **model** (`Model`)
      The fully resolved model definition, including metadata,
      configuration, signatures, assets, tags, and runtime information.

    - **invocation** (`Invocation`)
      Structured invocation object containing inputs, outputs,
      timestamps, and identifying metadata.
    """
    access_token: Sensitive[str]
    model: Model
    invocation: Invocation
