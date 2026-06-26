import requests
import json
class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        self.respose = requests.get(self.url)
        return self.response

    def load_json(self):
        self.data = self.respose.json()
        return self.data