import requests
import json

r = requests.get('http://45.40.137.37:88/test')

print (r.text)