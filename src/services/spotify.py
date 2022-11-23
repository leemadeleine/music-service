from src.clients.spotify import SpotifyClient

class SpotifyService:
    """
    Spotify Service
    """
    def __init__(self) -> None:
        self.spotify_client = SpotifyClient()

    def get_my_playlists(self, name: str):
        """
        Get playlists and extract the uri value
        """
        all_playlists = self.spotify_client.get_my_playlists()
        for item in all_playlists["items"]:
            if item["name"] == name:
                return item["uri"]

    def get_my_albums(self):
        """
        Get albums and extract the uri value
        """
        all_albums = self.spotify_client.get_my_albums()
        return all_albums
