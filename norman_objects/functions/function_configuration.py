from norman_objects.functions.function_state_reason_codes import FunctionStateReasonCodes
from norman_objects.functions.function_states import FunctionStates
from norman_objects.norman_base_model import NormanBaseModel


class FunctionConfiguration(NormanBaseModel):
    state: FunctionStates = FunctionStates.Unknown
    reason: str = "State reason is unknown."
    reason_code: FunctionStateReasonCodes = FunctionStateReasonCodes.Unknown
