from norman_objects.services.file_push.checksum.checksum_request import ChecksumRequest


class InputChecksumRequest(ChecksumRequest):
    invocation_id: str
