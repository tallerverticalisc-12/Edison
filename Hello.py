import requests
import json

r = requests.get('http://45.40.137.37:88/sensor')

print (r.text)