import requests
import json

r = requests.post('facebook.com', data = {'key':'value'})
r = requests.get('facebook.com')
r.json()