import requests
from config import Config

class APIClient:
    @staticmethod
    def get(endpoint, params=None, headers=None):
        url = f"{Config.BASE_URL}/{endpoint}"
        return requests.get(url, params=params, headers=headers)

    @staticmethod
    def post(endpoint, data, headers):
        url = f"{Config.BASE_URL}/{endpoint}"
        return requests.post(url, data=data, headers=headers)

    @staticmethod
    def put(endpoint,data, headers):
        url = f"{Config.BASE_URL}/{endpoint}"
        return requests.put(url, data=data, headers=headers)

    @staticmethod
    def delete(endpoint, headers):
        url = f"{Config.BASE_URL}/{endpoint}"
        return requests.delete(url, headers=headers)
