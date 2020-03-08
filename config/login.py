import json
import os
from getpass import getpass

import spotify_token


def load_file(open_mode="r"):
    cur_path = os.path.dirname(__file__)
    path = cur_path + "\\login.json"
    file = open(path, open_mode, encoding="utf8")
    return file


def request_login_info():
    print("[Login to your Spotify account!]")
    print("Not that your Account need to be Premium to work properly.")
    username = input("Username/e-mail: ")
    password = getpass("Password: ")
    save_in_json(username, password)


def save_in_json(username, password):
    input_login = {
        "username": username,
        "password": password
    }
    file = load_file("w")
    json.dump(input_login, file)
    file.close()

    # print(json_file)


def get_user_token():
    file = load_file()
    credentials = json.loads(file)
    token = spotify_token.start_session(credentials["username"],
                                        credentials["password"])
    return token[0]


request_login_info()
input()
