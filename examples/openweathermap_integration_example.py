#!/usr/bin/env python
import sys
sys.path.append("./")
sys.path.append("../")
import requests
from utils import get_api_keys
import json
import ujson

api_keys = get_api_keys("../api_keys.txt")
openweathermap_api_key = api_keys["openweathermap_api_key"]
api_end_point = "http://api.openweathermap.org/data/2.5/weather?q=riyadh" + \
                "&APPID=" + openweathermap_api_key

response = requests.get(api_end_point)
j = ujson.loads(response.text)
print json.dumps(j, sort_keys=True, indent=2, separators=(",", ": "))
