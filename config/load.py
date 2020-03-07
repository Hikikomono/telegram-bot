import json
import os


def load_token():
    """Loads the json file that contains the API token.
    :returns the API token"""
    cur_path = os.path.dirname(__file__)
    new_path = cur_path + "\\api_token.json"
    try:
        file = open(new_path, "r", encoding="utf8")
    except FileNotFoundError:
        print('The "api_token.json" is missing. Put this file in the config folder before running the program.')
        raise
    try:
        json_file = json.load(file)["token"]
        return json_file
    except KeyError as e:
        raise KeyError("Missing token in {}!".format(new_path)) from e

# print(load_token())
