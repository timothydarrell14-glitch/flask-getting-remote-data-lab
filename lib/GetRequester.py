import requests
from flask import make_response, request, current_app

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
response = requests.get(url)
data = response.json()
class GetRequester:

    def __init__(self, url):
        global response, data
        self.url = url
        self.data = data
        self.response = response

    def get_response_body(self):
        host = request.headers.get('Host')
        appname = current_app.name
        response_body = f"""
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
    """
        return make_response(response_body, 200, {})

    def load_json(self):
        return data

c1 = GetRequester(url)