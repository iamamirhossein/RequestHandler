import requests


class RequestHandler:
    """
        with exception handling
    """

    def __init__(self) -> None:
        self._response = None
        self._url = None
        self._expected_status = 200

    def send(self, url, expected_status, method='get', raise_exception=False, **kwargs):
        self._expected_status = expected_status
        self._url = url
        try:
            response = requests.request(method=method, url=url, **kwargs)
            self._response = response
            if response.status_code != expected_status:
                content = response.content
                try:
                    content = response.json()
                except Exception as ex:
                    pass
                # can set logger
            return response
        except requests.RequestException as ex:
            # can set logger
            if raise_exception:
                raise ex
            response = requests.Response()
            response.status_code = 504
            response._content = bytes('{"error": true, "detail": "' + str(ex) + '"}', 'utf-8')
            self._response = response
            return response
