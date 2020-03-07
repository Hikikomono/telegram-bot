import json
import os


def load_token() -> str:
    """Loads the json file that contains the API token.
    :returns the API token"""
    cur_path = os.path.dirname(__file__)
    new_path = cur_path + "\\api_token.json"

    file =open(new_path, "r", encoding="utf8")
    json_file = json.load(file)
    return json_file["token"]

# print(load_token())
# print(load_token()["token"])