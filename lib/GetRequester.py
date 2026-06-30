import requests
from flask import jsonify

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return jsonify(response), 200

    def load_json(self):
        data = requests.get(url).json()
        return data
    
GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")