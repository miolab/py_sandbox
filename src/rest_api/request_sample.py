import requests

URL = 'https://jsonplaceholder.typicode.com/'


def get() -> requests.models.Response:
    route = 'todos'
    payload = {
        'id': 1
    }

    return requests.get(
        f'{URL}{route}',
        params=payload
    )


if __name__ == '__main__':
    print(type(get()))
    print(get().status_code)
    print(get().text)
    print(get().json())
