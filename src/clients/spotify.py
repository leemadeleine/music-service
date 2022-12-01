import requests
from requests.auth import HTTPBasicAuth
import os
from urllib.parse import urlencode

BASE_URI = "https://api.spotify.com"
ACCOUNTS_BASE_URI = "https://accounts.spotify.com"
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
albums_token = os.environ["TOKEN_ALBUMS"]
playlists_token = os.environ["TOKEN_PLAYLISTS"]


class SpotifyClient:
    """
    Spotify Client
    """

    def __init__(self, token) -> None:
        self.token = token

    def get_my_albums(self) -> any:
        """
        Get top albums (default 20) for the account associated with the passed token
        """
        response = requests.get(
            BASE_URI + "/v1/me/albums",
            headers={"Authorization": "Bearer " + self.token},
            timeout=10,
        )
        return response.json()

    def get_my_playlists(self) -> any:
        """
        Get top 3 playlists for the account associated with the passed token
        """
        response = requests.get(
            BASE_URI + "/v1/me/playlists?limit=3",
            headers={"Authorization": "Bearer " + self.token},
            timeout=10,
        )
        return response.json()

    def get_playlists(self):
        """
        get maddie's playlists
        """
        uri = BASE_URI + "/v1/users/spotify/playlists?limit=50"
        response = requests.get(
            uri,
            headers={"Authorization": "Bearer " + self.token},
            timeout=10,
        )
        return response.json()

    def get_recommendations(self, query_params):
        """
        get recs based on params defined in mood_map.py
        """
        uri = BASE_URI + "/v1/recommendations?" + urlencode(query_params)
        uri = uri.replace('%2C', ',')
        response = requests.get(
            uri,
            headers={"Authorization": "Bearer " + self.token},
            timeout=10,
        )
        return response.json()

    # Using the accounts API

    def get_auth_token(self, code):
        """
        get auth token
        """

        uri = ACCOUNTS_BASE_URI + "/api/token"

        response = requests.post(
            uri,
            data={
                "grant_type": "client_credentials",
                "code": code,
                "redirect_uri": "http://localhost:3000",
            },
            auth=HTTPBasicAuth(client_id, client_secret),
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
            timeout=10,
        )
        return response.json()
