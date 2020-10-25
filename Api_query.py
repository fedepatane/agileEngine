import requests
import json
from pymemcache.client import base

class API_query:

    def __init__(self, url, cache_connection):
        self.url = url
        self.cache = cache_connection
        self.ids = []

    def getImages(self, num_page):

        res = self.cache.get("page_" + str(num_page))
        if res is None :

            #token = client.get('token')
            token = "acc910f986314bc6d05f98851e9f562c72641712"
            headers = {"Authorization": "Bearer " + token}

            # fijarse primero si esta cacheado y sino ir a la app
            url = self.url + 'images?page=' + str(num_page)

            x = requests.get(url,  headers = headers)
            res =  json.loads(x.text)

            #aca tenemos q guardar en la cache , el resultado de el numero de pagina y ademas cada foto por separado
            self.cache["page_" + str(num_page)] = res


        return res

    def getImage(self, id):
        result = self.cache.get(id)

        if result is None:
            token = self.cache.get('token')
            headers = {"Authorization": "Bearer " + token}

            # fijarse primero si esta cacheado y sino ir a la app
            url = self.url + 'images/' + str(id)

            x = requests.get(url, headers = headers)
            result = json.loads(x.text)

            self.cache[id] = result
            self.ids.append(id)

        return result


    def search(self, searchTerm):
        ## search term is {key : value }
        res = []
        searchTerm =  json.loads(searchTerm)

        for key_term, value_term in searchTerm.items():
            key = key_term
            value = value_term

        for id in self.ids :
            pic = self.cache.get(id)
            if pic[key] == value :
                res.append(pic)
            else :
                if key == "tags" :
                    #tenemos q ver a cual tag esta buscando
                    tags = pic["tags"].split(" ")
                    if value in tags :
                        res.append(pic)

        return res
