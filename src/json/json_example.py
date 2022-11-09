import json
from typing import Any

fruits: dict[
    str, list[dict[str, int | str]]
] = {
    "fruits":
        [
            {"id": 111, "name": "apple"},
            {"id": 222, "name": "orange"}
        ]
}


def gen_json_from_dict(dictionary: dict[str, Any]) -> str:
    return json.dumps(dictionary)


def gen_dict_from_json(json_string: str) -> dict[str, Any]:
    return json.loads(json_string)


def gen_json(path: str) -> None:
    """Generate new JSON file.

    example:
    - execute
        - `gen_json('src/json/sample.json')`
    - result
        - a new JSON file generated as
        `{"fruits": [{"id": 111, "name": "apple"}, {"id": 222, "name": "orange"}]}`
    """
    with open(path, 'w') as f:
        json.dump(fruits, f)


if __name__ == '__main__':
    gen_json('src/json/sample.json')
