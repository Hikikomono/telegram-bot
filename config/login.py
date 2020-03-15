import json
import os

import spotify_token
from requests import HTTPError


def load_file(open_mode="r"):
    cur_path = os.path.dirname(__file__)
    path = cur_path + "\\login.json"
    file = open(path, open_mode, encoding="utf8")
    return file


def request_login_info() -> dict:
    print("[Login to your Spotify account!]")
    print("Note, that your account needs to be Premium to work properly.")
    username = input("Username/e-mail: ")
    # password = getpass("Password: ")
    password = input("Password: ")
    return {'username': username, 'password': password}  # this is a dict()


def save_in_json(token: list):
    input_token = {
        "token": token[0],
        "expiration_date": token[1]
    }
    file = load_file("w")
    json.dump(input_token, file)
    file.close()

    # print(json_file)


def request_user_token(credentials: dict) -> list:
    token = spotify_token.start_session(credentials["username"],
                                        credentials["password"])
    return token


def get_user_token() -> str:
    file = load_file()
    try:
        json_file = json.load(file)
    except KeyError as e:
        raise KeyError("You are not logged into your Spotify account!") from e
    token = json_file["token"]
    file.close()
    return token


def load_new_user_token():
    while True:
        login_credentials = request_login_info()
        try:
            token = request_user_token(login_credentials)
            save_in_json(token)
            break
        except HTTPError:
            print("Login failed! Please reenter Login-Credentials.\n\n")
            continue


# print(get_user_token())
# load_new_user_token()
