from norman_objects.shared.requests.get_models_request import GetModelsRequest


class SearchRequest(GetModelsRequest):
    query: str
