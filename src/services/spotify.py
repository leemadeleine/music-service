import os

from src.clients.spotify import SpotifyClient
from src.services.mood_map import mood_map


class SpotifyService:
    """
    Formatting data fetched using the Spotify Client
    """

    def __init__(self, code=None, token=None) -> None:
        self.spotify_client = SpotifyClient(token)
        self.token = token
        self.code = code

    def get_credentials(self):
        """
        Get credentials for spotify app
        """
        return {
            "client_id": os.environ["CLIENT_ID"],
            "client_secret": os.environ["CLIENT_SECRET"],
        }

    def get_token(self):
        """
        Get auth token for spotify app
        """
        return self.spotify_client.get_auth_token(self.code)

    def get_recommendations(self, mood):
        """
        get recommendations from mood based parameters
        """
        return self.spotify_client.get_recommendations(query_params=mood_map[mood])
