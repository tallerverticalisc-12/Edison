import requests
import json

r = requests.post('http://45.40.137.37:88/sensor', data = {'key':'value'})
r = requests.get('http://45.40.137.37:88/sensor')
r.json()