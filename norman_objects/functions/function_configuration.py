from norman_objects.functions.function_state_reason_code import FunctionStateReasonCode
from norman_objects.functions.function_state import FunctionState
from norman_objects.norman_base_model import NormanBaseModel


class FunctionConfiguration(NormanBaseModel):
    state: FunctionState = FunctionState.NotProvided
    reason: str = "State reason not provided."
    reason_code: FunctionStateReasonCode = FunctionStateReasonCode.NotProvided
