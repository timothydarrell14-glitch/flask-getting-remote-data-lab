import requests

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
response = requests.get(url)
data = response.json()
class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        return response

    def load_json(self):
        return data