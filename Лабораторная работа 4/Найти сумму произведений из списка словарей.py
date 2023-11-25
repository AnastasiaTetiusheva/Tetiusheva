# TODO решите задачу

import json

INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE, "r") as f:
        json_data = json.load(f)
        product = [item["score"] * item["weight"] for item in json_data]
        total_sum = sum(product)
        result = round(total_sum, 3)
        return result


print(task())




