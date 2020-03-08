import json
import os
from getpass import getpass


def load_file():
    cur_path = os.path.dirname(__file__)
    path = cur_path + "\\login.json"
    file = open(path, "w", encoding="utf8")
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
    file = load_file()
    json.dump(input_login, file)

    # print(json_file)


request_login_info()
input()
