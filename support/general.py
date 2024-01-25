import json

def is_valid_json(data):
    try:
        json_object = json.loads(data)
        if isinstance(json_object, list):
            return len(json_object) > 0
        return False
    except ValueError as e:
        return False
