# coding=utf-8
class StitchdataError(Exception):
    """Base exception for custom errors."""


class APIException(StitchdataError):
    """Indicates an API Exception has occured."""
    def __init__(self, *args, **kwargs):
        self.http_status_code = kwargs.get('status_code')
        super().__init__(*args)
