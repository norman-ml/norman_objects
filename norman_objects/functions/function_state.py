from norman_objects.functions.function_state_reasons_codes import FunctionStateReasonsCodes
from norman_objects.functions.function_states import FunctionStates
from norman_objects.norman_base_model import NormanBaseModel


class FunctionState(NormanBaseModel):
    state: FunctionStates = FunctionStates.Unknown
    reason: str = "State reason is unknown."
    reason_code: FunctionStateReasonsCodes = FunctionStateReasonsCodes.Unknown
