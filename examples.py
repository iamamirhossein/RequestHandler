from request_handler import RequestHandler


def get_gender_success():
    url = "https://api.genderize.io/"
    payload = {
            "name": "amir"
        }

    cls = RequestHandler()
    response = cls.send(url=url, method="get", expected_status=200, raise_exception=True, headers={}, params=payload)
    if response.status_code == 200:
        return f"status: {response.status_code} and json: {response.json()}"
    cls.raise_invalid_status(response=response)

