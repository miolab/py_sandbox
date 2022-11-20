import requests

URL = 'https://jsonplaceholder.typicode.com/'


def main():
    # return _get()
    return _post()


def _get() -> requests.models.Response:
    """Execute GET request.
    """
    route = 'posts'
    payload = {
        'id': 1
    }

    return requests.get(
        f'{URL}{route}',
        params=payload
    )


def _post() -> requests.models.Response:
    """Execute mock POST request.
    """
    route = 'posts'
    payload = {
        'id': 1,
        'title': 'sample title',
        'body': 'sample body'
    }
    return requests.post(
        f'{URL}{route}',
        data=payload
    )


if __name__ == '__main__':
    print(type(main()))
    print(main().status_code)
    print(main().text)
    print(main().json())
