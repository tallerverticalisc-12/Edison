import requests

r = requests.post('http://45.40.137.37.88/sensor', data = {'key':'value'})

s = requests.get('http://45.40.137.37.88/sensor')

print s;