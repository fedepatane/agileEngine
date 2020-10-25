import requests
import json

class Connector:
    def __init__(self, apiKey, url, cache_connection):
        self.apiKey = apiKey
        self.url = url
        self.cache = cache_connection

    def connect(self):
        body =  { "apiKey": self.apiKey }
        x = requests.post(self.url, json=body)
        resp = json.loads(x.text)
        if (resp["token"] is None):
            return False

        token = resp["token"]
        self.cache['token'] = token

        return True
