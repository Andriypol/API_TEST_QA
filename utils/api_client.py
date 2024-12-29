import requests

class APIClient():

    BASE_URL = "https://gorest.co.in"
    auth_token = "Bearer 34968729db6fdd0944614cf5d2c4bc5c51474f9a60e928d36"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"{self.auth_token}"
        }

    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response

    def post(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def put(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, headers=self.headers, json=data)
        return response

    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url, headers=self.headers)
        return response
