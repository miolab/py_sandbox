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
