import json
import requests

url = 'http://45.40.137.37.88/sensor'
data = {'a': 10, 'b': [{'c': True, 'd': False}, None]}
headers = {'Content-Type': 'application/json'}

r = requests.post(url, data=json.dumps(data), headers=headers)

print json.dumps(r.json(), indent=4)