import json
from collections import namedtuple
from datetime import datetime


def get(file):
    try:
        with open(file, encoding="utf8") as data:
            return json.load(
                data, object_hook=lambda d: namedtuple("X", d.keys())(*d.values())
            )
    except:
        print(f"Error, could not locate {file}")