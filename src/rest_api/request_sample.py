import requests

URL = 'https://jsonplaceholder.typicode.com/'


def main():
    # return _get()
    # return _post()
    return _delete()


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


def _delete() -> requests.models.Response:
    """Execute mock DELETE request.
    """
    route = 'posts/1'
    payload = {
        'id': 1
    }
    return requests.delete(
        f'{URL}{route}',
        data=payload,
        timeout=3
    )


if __name__ == '__main__':
    print(type(main()))
    print(main().status_code)
    print(main().text)
    print(main().json())
