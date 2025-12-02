from norman_objects.shared.errors.api_errors.norman_api_error import NormanApiError


class NotFoundError(NormanApiError):
    status_code: int = 404
    error_type: str = "not_found"
    suggestions: list[str] = [
        "Verify the resource ID is correct",
        "Check if the resource has been deleted",
        "Ensure you have access to this resource",
    ]
