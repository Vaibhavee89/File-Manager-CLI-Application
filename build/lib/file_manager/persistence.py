# This would be used to handle file I/O operations and data persistence

import json
import os

FILE_PATH = "data/files.json"

def save_data(data):
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    if not os.path.exists(FILE_PATH):
        return {}

    try:
        with open(FILE_PATH, "r") as f:
            content = f.read().strip()
            if not content:  # empty file
                return {}
            return json.loads(content)
    except (json.JSONDecodeError, ValueError):
        # If file is corrupted or unreadable JSON
        return {}
