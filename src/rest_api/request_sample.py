import requests

URL = 'https://jsonplaceholder.typicode.com'

r = requests.get(f'{URL}/todos/1')

print(r.status_code)
