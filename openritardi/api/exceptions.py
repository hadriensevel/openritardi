"""Custom exceptions for the API.
"""


class VoidResponse(Exception):
    """Exception raised when the API returns a void response.
    """
    pass


class ErrorResponse(Exception):
    """Exception raised when the API returns an error.
    """
    pass
