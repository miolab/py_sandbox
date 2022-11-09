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
    """Generate JSON from dict.
    """
    return json.dumps(dictionary)


def gen_dict_from_json(json_string: str) -> dict[str, Any]:
    """Generate dict from JSON.
    """
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


def read_json(path: str) -> Any:
    """Read JSON file.

    - usage
        - `read_json('src/json/sample.json')`
    """
    with open(path, 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    sample_json = read_json('src/json/sample.json')

    print(gen_json_from_dict(sample_json))
