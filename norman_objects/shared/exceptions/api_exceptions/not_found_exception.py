from norman_objects.shared.exceptions.api_exceptions.norman_api_exception import NormanApiException


class NotFoundException(NormanApiException):
    status_code: int = 404
    error_type: str = "not_found"
    suggestions: list[str] = [
        "Verify the resource ID is correct",
        "Check if the resource has been deleted",
        "Ensure you have access to this resource",
    ]
