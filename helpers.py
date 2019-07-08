import json
from collections import namedtuple


def laod_json(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return dict()


def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def convert(item):
    try:
        if item not in globals() and item not in locals():
            return eval(item)

    except NameError:
        return item
