import requests
import os

BASE_URI = "https://api.spotify.com"
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
albums_token = os.environ["TOKEN_ALBUMS"]
playlists_token = os.environ["TOKEN_PLAYLISTS"]


class SpotifyClient:
    """
    Spotify Client
    """

    def __init__(self) -> None:
        pass

    def get_my_albums(self) -> any:
        """
        Get top albums (default 20) for the account associated with the passed token
        """
        response = requests.get(
            BASE_URI + "/v1/me/albums",
            headers={"Authorization": "Bearer " + albums_token},
            timeout=10,
        )
        return response.json()

    def get_my_playlists(self) -> any:
        """
        Get top 3 playlists for the account associated with the passed token
        """
        response = requests.get(
            BASE_URI + "/v1/me/playlists?limit=3",
            headers={"Authorization": "Bearer " + playlists_token},
            timeout=10,
        )
        return response.json()
