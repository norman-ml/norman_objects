from norman_objects.functions.function_state_reason_codes import FunctionStateReasonCode
from norman_objects.functions.function_states import FunctionState
from norman_objects.norman_base_model import NormanBaseModel


class FunctionConfiguration(NormanBaseModel):
    state: FunctionState = FunctionState.Unknown
    reason: str = "State reason is unknown."
    reason_code: FunctionStateReasonCode = FunctionStateReasonCode.Unknown
