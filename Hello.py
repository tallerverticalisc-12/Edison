import requests

r = requests.get('https://federacionhemofilia.azurewebsites.net')
print r.json() 