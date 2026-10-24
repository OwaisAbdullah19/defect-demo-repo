import json
from os.path import *

from app import config


def load_items(name):
    try:
        with open(join(config.DATA_DIR, name)) as fh:
            return json.load(fh)
    except:
        return []


def total(items):
    return sum(i.get("price", 0) for i in items)


def main():
    items = load_items("items.json")
    print("total:", total(items))


if __name__ == "__main__":
    main()
