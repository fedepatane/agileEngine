import requests
import json

from Api_query import *
from Connector import *

dict_cache = {"token": ""}

c = Connector("23567b218376f79d9415", 'http://interview.agileengine.com/auth', dict_cache)
connect = c.connect()

if (connect):
    api_query = API_query('http://interview.agileengine.com/', dict_cache)
    api_query.getImages(1)
    api_query.getImages(2)
    api_query.getImages(3)

    api_query.getImage("382e19a3cf6707cc8d7c")
    api_query.getImage("7755801b3a4847fa0b92")

    api_query.search('{"tags": "#beautifulday"}')

else :
    print("Error con api key identification ")
