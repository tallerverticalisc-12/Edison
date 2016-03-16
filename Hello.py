import requests

r = request.post('http://45.40.137.37.88/sensor', data = {'key':'value'})

s = request.get('http://45.40.137.37.88/sensor')

print s;