import requests
import json

r = requests.post('https://api.github.com/events', data = {'key':'value'})
r = requests.get('https://api.github.com/events')
r.json()