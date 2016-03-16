import requests
import json

r = requests.get('http://45.40.137.37:88/test')
s = requests.post('http://45.40.137.37:88/sensor', {"id":"2"})

print (r.text)
print (s.text)
