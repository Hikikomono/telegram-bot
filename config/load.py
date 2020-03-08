import json
import os


def get_path():
    cur_path = os.path.dirname(__file__)
    new_path = cur_path + "\\api_token.json"
    return new_path


def load():
    """Loads the json file that contains the API token.
    :returns the API token"""
    path = get_path()
    try:
        file = open(path, "r", encoding="utf8")
        return file
    except FileNotFoundError:
        print('The "api_token.json" is missing. Put this file in the config folder before running the program.')
        raise


def load_telegram_token():
    file = load()
    path = get_path()
    try:
        json_file = json.load(file)["telegram_token"]
        return json_file
    except KeyError as e:
        raise KeyError("Missing token in {}!".format(path)) from e

# print(load_token())
