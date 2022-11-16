import requests

URL = 'https://jsonplaceholder.typicode.com'

payload = {
    'id': 1
}

r = requests.get(
    f'{URL}/todos',
    params=payload
)

print(r.status_code)
print(r.text)
print(r.json())
