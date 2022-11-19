import requests

URL = 'https://jsonplaceholder.typicode.com/'


def main():
    return _get()


def _get() -> requests.models.Response:
    route = 'posts'
    payload = {
        'id': 1
    }

    return requests.get(
        f'{URL}{route}',
        params=payload
    )


if __name__ == '__main__':
    print(type(main()))
    print(main().status_code)
    print(main().text)
    print(main().json())
