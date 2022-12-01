import os

from src.clients.spotify import SpotifyClient
from src.services.mood_map import mood_map

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]


class SpotifyService:
    """
    Spotify Service
    """

    def __init__(self, code=None, token=None) -> None:
        self.spotify_client = SpotifyClient(token)
        self.token = token
        self.code = code

    def get_my_playlists(self, name: str):
        """
        Get playlists and extract the uri value
        """
        all_playlists = self.spotify_client.get_my_playlists()
        for item in all_playlists["items"]:
            if item["name"] == name:
                return item["uri"]

    def get_playlists(self):
        """
        get maddie's playlists
        """
        all_playlist_data = self.spotify_client.get_playlists()
        items = all_playlist_data["items"]
        cleaned_data = []
        for item in items:
            cleaned_data.append(
                {"uri": item["uri"], "src": item["external_urls"]["spotify"]}
            )

        return cleaned_data

    def get_my_albums(self):
        """
        Get albums and extract the uri value
        """
        all_albums = self.spotify_client.get_my_albums()
        return all_albums

    def get_credentials(self):
        """
        Get credentials for spotify app
        """
        return {"client_id": client_id, "client_secret": client_secret}

    def get_token(self):
        """
        Get auth token for spotify app
        """
        auth = self.spotify_client.get_auth_token(self.code)
        return auth

    def get_recommendations(self, mood):
        """
        get recs
        """
        recs = self.spotify_client.get_recommendations(query_params=mood_map[mood])
        return recs
