import requests


class RequestHandler:
    """
        with exception handling
    """

    def __init__(self)-> None:
        self._response = None
        self._url = None
        self._expected_status = 200
