import json

fruits: dict[
    str, list[dict[str, int | str]]
] = {
    "fruits":
        [
            {"id": 111, "name": "apple"},
            {"id": 222, "name": "orange"}
        ]
}

print(fruits)
print(json.dumps(fruits))


def gen_json(path: str) -> None:
    """Generate new JSON file
    """
    with open(path, 'w') as f:
        json.dump(fruits, f)


if __name__ == '__main__':
    gen_json('src/json/sample.json')
