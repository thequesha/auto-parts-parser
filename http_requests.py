import json
import requests


class HttpRequests:
    """Class For http requests"""

    def getCarToBeParsed(self):
        response = requests.get(
            url='http://127.0.0.1:8000/api/marks',
        )

        return response.json()

    def sendCarsList(self, cars):
        response = requests.post(
            url='http://127.0.0.1:8000/api/marks',
            json=cars
        )

        status = response.status_code

        return status
