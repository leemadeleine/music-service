import os
from urllib.parse import urlencode
import requests
from requests.auth import HTTPBasicAuth

BASE_URI = "https://api.spotify.com"
ACCOUNTS_BASE_URI = "https://accounts.spotify.com"


class SpotifyClient:
    """
    Client to interact with various Spotify APIs
    """

    def __init__(self, token) -> None:
        self.token = token

    def get_recommendations(self, query_params):
        """
        get recommendationss based on params defined in mood_map.py
        """
        uri = BASE_URI + "/v1/recommendations?" + urlencode(query_params)
        uri = uri.replace("%2C", ",")
        response = requests.get(
            uri,
            headers={"Authorization": "Bearer " + self.token},
            timeout=10,
        )
        return response.json()

    def get_auth_token(self, code):
        """
        Client credentials authorization method
        """

        uri = ACCOUNTS_BASE_URI + "/api/token"

        response = requests.post(
            uri,
            data={
                "grant_type": "client_credentials",
                "code": code,
                "redirect_uri": "http://localhost:3000",
            },
            auth=HTTPBasicAuth(os.environ["CLIENT_ID"], os.environ["CLIENT_SECRET"]),
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
            timeout=10,
        )
        return response.json()
