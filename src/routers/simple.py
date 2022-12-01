from fastapi import APIRouter
from src.services.spotify import SpotifyService

router = APIRouter(
    prefix="/simple",
)


@router.get("/happy")
async def get_happy(token: str = None):
    """
    Return spotify uri id matching a happy playlist
    """
    spotify_service = SpotifyService(None, token)
    return {"uri": spotify_service.get_my_playlists("Happy Music")}


@router.get("/sad")
async def get_sad(token: str = None):
    """
    Return spotify uri id matching a sad playlist
    """
    spotify_service = SpotifyService(None, token)
    return {"uri": spotify_service.get_my_playlists("Sad Music")}


@router.get("")
async def get_playlist_data(token: str = None):
    """
    Return top 50 spotify playlists data
    """
    spotify_service = SpotifyService(None, token)
    return {"data": spotify_service.get_playlists()}


@router.get("/recommendations")
async def get_recos(token: str = None, mood: str = None):
    """
    get recommendations based on set of inputs
    """
    spotify_service = SpotifyService(None, token)
    return {"data": spotify_service.get_recommendations(mood)}
