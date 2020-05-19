import requests
import pprint


# response = requests.get('http://127.0.0.1:8000/api/v0/mesto/', auth = ('Ildarets', '9205ildar'))

token = 'df56a36ffb2af5566313e245ed75320ef01ee9cd'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/mesto/', headers = headers)

pprint.pprint(response.json())