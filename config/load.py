import json
import os

import spotipy
from spotipy import SpotifyClientCredentials


def get_path():
    cur_path = os.path.dirname(__file__)
    new_path = cur_path + "\\api_token.json"
    return new_path


def load():
    """Loads the .json file
    :returns the .json file"""
    path = get_path()
    try:
        file = open(path, "r", encoding="utf8")
        return file
    except FileNotFoundError:
        print('The "api_token.json" is missing. Put this file in the config folder before running the program.')
        raise


def load_spotify_token():
    """:returns ready Spotify object"""
    file = load()
    path = get_path()

    try:
        json_file = json.load(file)
    except KeyError as e:
        raise KeyError("Missing Spotify token in {}!".format(path)) from e

    cid = json_file["spotify_client_id"]
    secret = json_file["spotify_client_secret"]
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return spotify


def load_telegram_token():
    """:returns the 'Telegram API-Token'"""
    file = load()
    path = get_path()
    try:
        json_file = json.load(file)["telegram_token"]
        return json_file
    except KeyError as e:
        raise KeyError("Missing Telegram token in {}!".format(path)) from e

# print(load_spotify_token())
