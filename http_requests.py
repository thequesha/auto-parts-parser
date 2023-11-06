import json
import requests


class HttpRequests:
    """Class For http requests"""

    def getCarToBeParsed(self):
        response = requests.get(
            url='http://216.250.11.83:8800/api/marks',
        )

        return response.json()

    def sendCarsList(self, cars):
        response = requests.post(
            url='http://216.250.11.83:8800/api/marks',
            json=cars
        )

        status = response.status_code

        return status
    
    def sendData(self, data):
        
        
        with open('data.json', 'w') as fp:
            json.dump(data, fp, sort_keys=True, indent=4)
        
        response = requests.post(
            url='http://216.250.11.83:8800/api/all-data',
            json=data
        )
        
        status = response.status_code

        return status
  